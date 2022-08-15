from pibot.base.digitalin import DigitalInput
import RPi.GPIO as GPIO


class RpiInput(DigitalInput):
    def __init__(self, pin):
        super().__init__()
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def get(self):
        return bool(GPIO.input(self.pin))
