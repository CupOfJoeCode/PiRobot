from pibot.vision import *
import cv2


class Robot:
    def __init__(self):
        self.data = {
        }
        self.running = False
        self.vision = Capture()
        self.camera_frame = self.vision.get_frame()

    def run(self):
        target, frame, mask = self.vision.get_target()
        self.camera_frame = self.vision.get_frame()

    def stop(self):
        pass

    def trigger_start(self, trigger):
        pass

    def trigger_end(self, trigger):
        pass
