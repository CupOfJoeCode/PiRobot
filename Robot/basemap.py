from pibot.base.motor import Motor


class DebugMotor(Motor):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def set(self, speed):
        self.speed = speed
        print(f'{self.name} set to {speed}')


class BaseMap:

    def __init__(self):
        pass

    def get_left_motor(self):
        return DebugMotor('Left')

    def get_right_motor(self):
        return DebugMotor('Right')
