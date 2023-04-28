from pibot.base.commands.command import Command


class BaseRobot:
    def __init__(self) -> None:
        self.data = {}
        self.running = False

        self.triggers = {}
        self.binds = {}

    def run(self) -> None:
        for bind in self.binds:
            if self.triggered(bind):
                self.binds[bind].run()

            elif self.binds[bind].started:
                self.binds[bind].stop()
                self.binds[bind].reset()

    def stop(self) -> None:
        pass

    def bind(self, trigger: str, command: Command) -> None:
        self.binds[trigger] = command

    def triggered(self, trigger: str) -> bool:
        if trigger not in self.triggers:
            return False
        return self.triggers[trigger]

    def trigger_start(self, trigger: str) -> None:
        self.triggers[trigger] = True

    def trigger_end(self, trigger: str) -> None:
        self.triggers[trigger] = False
