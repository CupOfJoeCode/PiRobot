from dataclasses import dataclass
import cv2
import numpy as np


@dataclass
class VisionTarget:
    x: float
    y: float
    radius: float
    width: int
    height: int


def blank_image():
    return np.array(
        [[[0, 0, 0]]]
    )


def get_target_from_mask(mask):
    height = len(mask)
    width = len(mask[0])
    poses = np.argwhere(mask == 255)
    if poses.any():
        pos = np.mean(poses, axis=0)
        maxs = np.max(poses, axis=0)
        mins = np.min(poses, axis=0)

        radius = (maxs[0]-mins[0] + maxs[1]-maxs[1]) // 2
        radius = max(radius, 1)
        return VisionTarget(
            (pos[1]/width)*2-1,
            (pos[0]/height)*2-1,
            radius/width,
            width,
            height
        )
    return None


class MotionCapture:
    def __init__(self):
        self.filter = 60
        self.cap = cv2.VideoCapture(0)
        self.threshold = 0
        self.filtered_frame = None
        self.prev_frame, _ = self.get_frame()

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_frame(self):
        _, rawframe = self.cap.read()
        frame = cv2.cvtColor(rawframe, cv2.COLOR_BGR2GRAY)

        if self.filtered_frame is None:
            self.filtered_frame = frame

        self.filtered_frame = (self.filtered_frame *
                               (self.filter-1) + frame) * (1/self.filter)
        return self.filtered_frame.astype(np.uint8), rawframe

    def get_target(self):
        frame, raw = self.get_frame()
        dif = np.absolute(frame - self.prev_frame)

        thresh = np.where(dif > self.threshold, 255, 0).astype(np.uint8)

        self.prev_frame = frame

        return get_target_from_mask(thresh), raw, thresh


class Capture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.target_color = [0, 0, 0]
        self.color_threshold = 0

    def get_target_min_max(self):
        return np.array(
            [self.target_color[2]-self.color_threshold,
             self.target_color[1]-self.color_threshold,
             self.target_color[0]-self.color_threshold]), np.array(
            [self.target_color[2]+self.color_threshold,
             self.target_color[1]+self.color_threshold,
             self.target_color[0]+self.color_threshold])

    def set_target_color(self, red, green, blue, threshold):
        self.target_color = [red, green, blue]
        self.color_threshold = threshold

    def get_frame(self):
        _, frame = self.cap.read()
        return frame

    def get_target(self):
        frame = self.get_frame()

        min_color, max_color = self.get_target_min_max()
        mask = cv2.inRange(frame, min_color, max_color)

        return get_target_from_mask(mask), frame, mask
