import RPi.GPIO as GPIO
import time

# Moves a servo when a microphone is connected

# GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(18, GPIO.HIGH)

# Servo code
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50)

def callback(channel):
	if GPIO.input(channel):
		print "Sound detected"
		moveServo()
	else:
		print "Sound detected"
		moveServo()

def moveServo():
	print "Moving servo"
	p.start(0)
	p.ChangeDutyCycle(3)
	time.sleep(1)
	p.ChangeDutyCycle(12)
	time.sleep(1)
	p.stop()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) # tells us when the pin is high or low

GPIO.add_event_callback(channel, callback)

while True:
	time.sleep(1)
