import RPi.GPIO as GPIO





# RGB pins (BOARD numbering)


bluePin = 11
greenPin = 15
redPin = 13
fiveVPin = 16





GPIO.setmode(GPIO.BOARD)





GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(fiveVPin, GPIO.OUT)





def all_off():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)
    GPIO.setup(fiveVPin, GPIO.LOW)





all_off()