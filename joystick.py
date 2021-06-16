import RPi.GPIO as GPIO
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)


pins = [29, 31, 33, 32, 36, 38]
for p in pins:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)


GPIO.output(33, GPIO.HIGH)

GPIO.output(32, GPIO.HIGH)


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_up(self, value):
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(31, GPIO.LOW)

    def on_L3_down(self, value):
        GPIO.output(29, GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)

    def on_L3_y_at_rest(self):
        GPIO.output(29, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)

    def on_R3_up(self, value):
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)

    def on_R3_down(self, value):
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)

    def on_R3_y_at_rest(self):
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)

