from dataclasses import dataclass
import cv2
import numpy as np


@dataclass
class VisionTarget:
    x: float
    y: float
    radius: float


class Capture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.target_color = [0, 0, 0]
        self.color_threshold = 0

    def get_target_min_max(self):
        return np.array(
            self.target_color[2]-self.color_threshold,
            self.target_color[1]-self.color_threshold,
            self.target_color[0]-self.color_threshold), np.array(
            self.target_color[2]+self.color_threshold,
            self.target_color[1]+self.color_threshold,
            self.target_color[0]+self.color_threshold)

    def set_target_color(self, red, green, blue, threshold):
        self.target_color = [red, green, blue]
        self.color_threshold = threshold

    def get_frame(self):
        _, frame = self.cap.read()
        return frame

    def get_target_pos_radius(self):
        frame = self.get_frame()

        min_color, max_color = self.get_target_min_max()
        mask = cv2.inRange(frame, min_color, max_color)
        width = len(mask)
        height = len(mask[0])
        poses = np.argwhere(mask == 255)
        if poses.any():
            pos = np.mean(poses, axis=0)
            maxs = np.max(poses, axis=0)
            mins = np.min(poses, axis=0)

            radius = (maxs[0]-mins[0] + maxs[1]-maxs[0]) // 4
            radius = max(radius, 1)
            return VisionTarget(
                (pos[1]/height)*2-1,
                (pos[0]/width)*2-1,
                radius/width
            )
        return None
