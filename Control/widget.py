import pygame as pg


class DataWidget:
    def __init__(self) -> None:
        self.title = ""
        self.text = ""
        self.background = (255, 255, 255)
        self.font = pg.font.Font(None, 32)
        self.entry_type = 0

    def get_surface(self):
        out_surface = pg.Surface((128, 128))
        out_surface.fill(self.background)
        pg.draw.rect(out_surface, (60, 60, 200), (0, 0, 128, 32))
        title_surf = self.font.render(self.title, True, (200, 200, 200))
        out_surface.blit(title_surf, (4, 4))
        value_surf = self.font.render(self.text, True, (60, 60, 60))
        out_surface.blit(value_surf, (4, 40))
        return out_surface

    def set_title(self, title):
        self.title = title

    def set_value(self, data, entry_type):
        if entry_type == 1:
            self.background = (200, 60, 60) if (data == "1") else (60, 30, 30)
            self.text = ""
            self.isbool = True
        else:
            self.text = str(data)
            self.isbool = False
