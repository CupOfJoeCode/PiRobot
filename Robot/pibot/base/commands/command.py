class Command:
    def __init__(self, name) -> None:
        self.name = name
        self.initialize_handler = lambda: None
        self.execute_handler = lambda: None
        self.until_handler = lambda: True
        self.end_handler = lambda: None
        self.running = True
        self.started = False

    def run(self) -> None:
        if not self.running:
            return
        if not self.started:
            self.started = True
            self.initialize_handler()
            return
        self.execute_handler()
        if self.until_handler():
            self.end_handler()
            self.running = False

    def reset(self) -> None:
        self.running = True
        self.started = False

    def stop(self) -> None:
        self.running = False
        self.end_handler()

    def initialize(self, handler: callable) -> None:
        self.initialize_handler = handler
        return self

    def execute(self, handler: callable):
        self.execute_handler = handler
        return self

    def until(self, handler: callable):
        self.until_handler = handler
        return self

    def end(self, handler: callable):
        self.end_handler = handler
        return self

    def with_name(self, name: str):
        self.name = name
        return self

    def __repr__(self) -> str:
        return f"Command({self.name})"
