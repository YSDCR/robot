import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)

pins = [29, 31, 33, 32, 36, 38]
for p in pins:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)


GPIO.output(29, GPIO.HIGH)
GPIO.output(33, GPIO.HIGH)

GPIO.output(32, GPIO.HIGH)
GPIO.output(38, GPIO.HIGH)

time.sleep(1)

GPIO.cleanup()

