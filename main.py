import time
import argparse
import RPi.GPIO as GPIO

#gpio

# RGB pins (BOARD numbering)
RED = 11
GREEN = 15
BLUE = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

#basic-logic

def set_color(r, g, b):
    GPIO.output(RED, GPIO.HIGH if r else GPIO.LOW)
    GPIO.output(GREEN, GPIO.HIGH if g else GPIO.LOW)
    GPIO.output(BLUE, GPIO.HIGH if b else GPIO.LOW)

def all_off():
    set_color(0, 0, 0)

#patterns

def strobe(color, flashes=12, on=0.08, off=0.08):
    for _ in range(flashes):
        set_color(*color)
        time.sleep(on)
        all_off()
        time.sleep(off)

def police():
    for _ in range(6):
        strobe((1, 0, 0), flashes=3, on=0.06, off=0.04)
        strobe((0, 0, 1), flashes=3, on=0.06, off=0.04)

def rainbow():
    colors = [
        (1,0,0),
        (1,1,0),
        (0,1,0),
        (0,1,1),
        (0,0,1),
        (1,0,1),
    ]
    for c in colors:
        strobe(c, flashes=4, on=0.07, off=0.07)

def chase():
    colors = [
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,0,1),
    ]
    for c in colors:
        set_color(*c)
        time.sleep(0.2)
        all_off()

def alt_magenta_green():
    for _ in range(12):
        set_color(1,0,1)
        time.sleep(0.15)
        set_color(0,1,0)
        time.sleep(0.15)
    all_off()

def purple_stay():
    set_color(1, 0, 1) #CSH-COLOR

#Menu

MENU = """
'{tttttttttttttttttttttttt^ *tttt\ 
:@@@@@@@@@@@@@@@@@@@@@@@@@m d@@@@N`
:@@@@@@@@@@@@@@@@@@@@@@@@@m d@@@@N`
:@@@@@m:::::::::::::rQ@@@@m d@@@@N`
:@@@@@] vBBBBBBBBBN,`]oooo* d@@@@N`
:@@@@@] o@@@NNNQ@@@"`ueeee| d@@@@N`
:@@@@@] o@@&   ,||?`'Q@@@@m d@@@@N`
:@@@@@] o@@Q]tt{{{z-'Q@@@@QOQ@@@@N`
:@@@@@] o@@@@@@@@@@"'Q@@@@@@@@@@@N`
:@@@@@] ';;;;;;y@@@"'Q@@@@N7Q@@@@N`
:@@@@@] \KKe^^^a@@@"'Q@@@@m d@@@@N`
:@@@@@] o@@@@@@@@@@" _::::' d@@@@N`
:@@@@@] raaaaaaaaay..H####} d@@@@N`
:@@@@@#eeeeeeeeeeeeek@@@@@m d@@@@N`
:@@@@@@@@@@@@@@@@@@@@@@@@@m d@@@@N`
:@@@@@@@@@@@@@@@@@@@@@@@@@e K@@@@W`
 .........................` `....- 
RGB Strip Controller
---------------------
RS  Red strobe
GS Green strobe
BS  Blue strobe
MS  Magenta strobe
PS  Police strobe
RF  Rainbow flash
CC  Color chase
MG  Magenta / Green alternate
CSH  Purple stay (solid)
0  All off
q  Quit
"""

# argparse only for -h
parser = argparse.ArgumentParser(
    description="RGB Strip Controller",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=MENU
)
parser.parse_args()

#main loop

try:
    while True:
        print(MENU)
        choice = input("Select mode: ").strip().lower()

        if choice == "RS":
            strobe((1,0,0))
        elif choice == "GS":
            strobe((0,1,0))
        elif choice == "BS":
            strobe((0,0,1))
        elif choice == "MS":
            strobe((1,0,1))
        elif choice == "PS":
            police()
        elif choice == "RF":
            rainbow()
        elif choice == "CC":
            chase()
        elif choice == "MG":
            alt_magenta_green()
        elif choice == "CSH":
            purple_stay()
        elif choice == "0":
            all_off()
        elif choice == "q":
            break
        else:
            print("Invalid option")

finally:
    all_off()
    GPIO.cleanup()
    print("Clean exit.")
