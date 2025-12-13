import time
import argparse
import RPi.GPIO as GPIO

#gpio   

RED = 11
GREEN = 15
BLUE = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

#basic logic

def set_color(r, g, b):
    GPIO.output(RED, GPIO.HIGH if r else GPIO.LOW)
    GPIO.output(GREEN, GPIO.HIGH if g else GPIO.LOW)
    GPIO.output(BLUE, GPIO.HIGH if b else GPIO.LOW)

def all_off():
    set_color(0, 0, 0)

#pattern

def strobe_forever(color, on=0.08, off=0.08):
    while True:
        set_color(*color)
        time.sleep(on)
        all_off()
        time.sleep(off)

def police_forever():
    while True:
        for _ in range(3):
            set_color(1,0,0); time.sleep(0.06)
            all_off(); time.sleep(0.04)
        for _ in range(3):
            set_color(0,0,1); time.sleep(0.06)
            all_off(); time.sleep(0.04)

def rainbow_forever():
    colors = [
        (1,0,0),
        (1,1,0),
        (0,1,0),
        (0,1,1),
        (0,0,1),
        (1,0,1),
    ]
    while True:
        for c in colors:
            set_color(*c)
            time.sleep(0.15)
            all_off()
            time.sleep(0.05)

def chase_forever():
    colors = [(1,0,0), (0,1,0), (0,0,1), (1,0,1)]
    while True:
        for c in colors:
            set_color(*c)
            time.sleep(0.2)
            all_off()

def alt_magenta_green_forever():
    while True:
        set_color(1,0,1)
        time.sleep(0.15)
        set_color(0,1,0)
        time.sleep(0.15)

def purple_stay_forever():
    while True:
        set_color(1, 0, 1)
        time.sleep(1)

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
1  Red strobe
2  Green strobe
3  Blue strobe
4  Magenta strobe
5  Police strobe
6  Rainbow flash
7  Color chase
8  Magenta / Green alternate
9  Purple stay (solid)
0  All off
q  Quit

(Ctrl+C to stop a pattern and return to menu)
"""

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
        choice = input("Select mode: ").strip()

        try:
            if choice == "1":
                strobe_forever((1,0,0))
            elif choice == "2":
                strobe_forever((0,1,0))
            elif choice == "3":
                strobe_forever((0,0,1))
            elif choice == "4":
                strobe_forever((1,0,1))
            elif choice == "5":
                police_forever()
            elif choice == "6":
                rainbow_forever()
            elif choice == "7":
                chase_forever()
            elif choice == "8":
                alt_magenta_green_forever()
            elif choice == "9":
                purple_stay_forever()
            elif choice == "0":
                all_off()
            elif choice.lower() == "q":
                break
            else:
                print("Invalid option")

        except KeyboardInterrupt:
            all_off()
            print("\nPattern stopped. Returning to menu")

finally:
    all_off()
    GPIO.cleanup()
    print("Clean exit.")
