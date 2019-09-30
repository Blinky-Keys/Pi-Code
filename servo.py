import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(0)

p.ChangeDutyCycle(3)
time.sleep(1)
p.ChangeDutyCycle(12)
time.sleep(1)

p.stop()
GPIO.cleanup()
