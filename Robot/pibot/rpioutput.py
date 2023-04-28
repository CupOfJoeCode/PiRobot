from pibot.base.digitalout import DigitalOutput
import RPi.GPIO as GPIO


class RpiOutput(DigitalOutput):
    def __init__(self, pin: int) -> None:
        super().__init__()
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def write(self, state: bool) -> None:
        GPIO.output(self.pin, state)
