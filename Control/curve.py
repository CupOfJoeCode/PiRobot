from vecmath import Vector


class BezierCurve:
    def __init__(self, points: list[Vector]):
        self.points = points

    def get_point(self, timeframe: float):
        if len(self.points) == 1:
            return self.points[0]
        new_points = []
        for i in range(len(self.points) - 1):
            a = self.points[i]
            b = self.points[i + 1]
            new_points.append(a + (b - a) * timeframe)
        return BezierCurve(new_points).get_point(timeframe)
