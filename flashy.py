import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

while(1):

	# Uncomment print statements if you want to be annoying lol
	#print "Lights on"
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(25, GPIO.HIGH)
	time.sleep(0.05)

	#print "Lights off"
	GPIO.output(18, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
	time.sleep(0.05)
