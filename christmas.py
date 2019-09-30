import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Set up all the pins that we will be using
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(25, gpio.OUT)

while(1):
	# Pin 18
	gpio.output(18, gpio.HIGH)
	time.sleep(0.5)
	gpio.output(18, gpio.LOW)

	# Pin 23
	gpio.output(23, gpio.HIGH)
	time.sleep(0.5)
	gpio.output(23, gpio.LOW)

	# Pin 24
	gpio.output(24, gpio.HIGH)
	time.sleep(0.5)
	gpio.output(24, gpio.LOW)

	# Pin 25
	gpio.output(25, gpio.HIGH)
	time.sleep(0.5)
	gpio.output(25, gpio.LOW)
