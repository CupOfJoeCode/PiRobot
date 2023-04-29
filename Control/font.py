import pygame as pg


class Font:
    def __init__(self) -> None:
        self.font = pg.font.Font(None, 24)
        self.memo = {}

    def render(self, text: str) -> pg.Surface:
        if text not in self.memo:
            self.memo[text] = self.font.render(text, True, (200,) * 3, None)
        return self.memo[text]
