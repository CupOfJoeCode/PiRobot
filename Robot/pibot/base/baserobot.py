from pibot.vision import Capture

class BaseRobot:
    def __init__(self):
        self.data = {
        }
        self.running = False

        self.triggers = {}
        self.binds = {}

        self.vision = Capture()
        self.camera_target,self.camera_frame, _ = self.vision.get_target()

    def run(self):
        for bind in self.binds:
            if self.triggered(bind):
                self.binds[bind].run()
                
            elif self.binds[bind].started:
                self.binds[bind].stop()
                self.binds[bind].reset()
        self.camera_target, self.camera_frame, _ = self.vision.get_target()

    def stop(self):
        pass

    def bind(self,trigger,command):
        self.binds[trigger] = command

    def triggered(self,trigger):
        if trigger not in self.triggers:
            return False
        return self.triggers[trigger]

    def trigger_start(self, trigger):
        self.triggers[trigger] = True

    def trigger_end(self, trigger):
        self.triggers[trigger] = False