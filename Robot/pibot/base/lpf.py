class LowPassFilter:
    def __init__(self, cutoff, poles=1):
        self.buffers = [0] * poles
        self.cutoff = min(1.0, max(0.0, cutoff))

    def set_cutoff(self, cutoff):
        self.cutoff = min(1.0, max(0.0, cutoff))

    def get_cutoff(self):
        return self.cutoff

    def calculate(self, sample):
        for index, buf in enumerate(self.buffers):
            if index == 0:
                prev_buf = sample
            else:
                prev_buf = self.buffers[index-1]

            self.buffers[index] += self.cutoff * (prev_buf - buf)
        return self.buffers[-1]
