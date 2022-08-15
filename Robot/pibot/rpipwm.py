from pibot.base.pwmout import PWMOutput
import RPi.GPIO as GPIO


class RpiPWMOutput(PWMOutput):
    def __init__(self, pin, freq=100):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, freq)
        self.pwm.start(0)

    def set(self, width):
        self.pwm.ChangeDutyCycle(min(100, max(0, int(width * 100))))
