import pygame as pg
import easygui
from vecmath import Vector, Rotation2d
from curve import BezierCurve
import requests


class TableView:
    def __init__(self, font, server):
        self.font = font
        self.scroll_offset = 0
        self.server = server
        self.has_held = False

    def update(
        self, table, mouse_pos, mouse_rel, mouse_down, mouse_right, scroll, window_size
    ):
        surface = pg.Surface(window_size, pg.SRCALPHA)
        surface.fill((0,) * 4)
        in_window = False
        if mouse_pos[0] in range(window_size[0]) and mouse_pos[1] in range(
            window_size[1]
        ):
            in_window = True
            self.scroll_offset += scroll
            if mouse_right:
                self.scroll_offset -= mouse_rel[1] * (1 / 24)
        self.scroll_offset = max(0, self.scroll_offset)
        scr_y = 4 - int((self.scroll_offset * 24))
        for key in table:
            entry = table[key]
            if entry["type"] == 0:
                val = float(entry["value"])
                surface.blit(self.font.render(f"{key}: {round(val,2)}"), (4, scr_y))
            elif entry["type"] == 1:
                keysurf = self.font.render(key)
                val = entry["value"] == "1"
                bg = pg.Surface(keysurf.get_size())
                bg.fill((200, 60, 60) if val else (60, 0, 0))
                bg.blit(keysurf, (0, 0))
                surface.blit(bg, (4, scr_y))
            elif entry["type"] == 2:
                val = entry["value"]
                surface.blit(self.font.render(f"{key}: {val}"), (4, scr_y))

            if (
                in_window
                and mouse_down
                and mouse_pos[1] in range(scr_y, scr_y + 24)
                and not (self.has_held)
            ):
                self.has_held = True
                if entry["type"] == 0:
                    val = entry["value"]
                    new_val = easygui.enterbox("Enter a new value", "Edit Number", val)
                    if new_val is not None:
                        try:
                            fval = float(new_val)
                            requests.get(
                                f"{self.server}/set_data?type=0&value={fval}&key={key}"
                            )
                        except Exception:
                            pass

                elif entry["type"] == 1:
                    val = int(entry["value"] == "0")
                    requests.get(f"{self.server}/set_data?type=1&value={val}&key={key}")
                if entry["type"] == 2:
                    val = entry["value"]
                    new_val = easygui.enterbox("Enter a new value", "Edit Text", val)
                    if new_val is not None:
                        requests.get(
                            f"{self.server}/set_data?type=2&value={new_val}&key={key}"
                        )
            scr_y += 24
        if not mouse_down:
            self.has_held = False
        return surface


class Pose2dView:
    square = [
        Vector(-1, -1),
        Vector(1, -1),
        Vector(1, 1),
        Vector(-1, 1),
    ]

    def __init__(self, font):
        self.font = font
        self.names = []
        self.lines = []
        self.pan_x = 0
        self.pan_y = 0
        self.ppm = 50.0

    def update(
        self, table, mouse_pos, mouse_rel, mouse_down, mouse_right, scroll, window_size
    ):
        def pose2d_translate(vec):
            screen_x = window_size[0] // 2 - int((self.pan_x - vec.x) * self.ppm)
            screen_y = window_size[1] // 2 + int((self.pan_y - vec.y) * self.ppm)
            return (screen_x, screen_y)

        if mouse_pos[0] in range(window_size[0]) and mouse_pos[1] in range(
            window_size[1]
        ):
            if mouse_down:
                self.pan_x -= mouse_rel[0] / self.ppm
                self.pan_y += mouse_rel[1] / self.ppm
            if scroll == 1:
                self.ppm /= 1.1
            elif scroll == -1:
                self.ppm *= 1.1
            if mouse_right:
                line_names = [",".join(point) for point in self.lines]
                line_names = ";".join(line_names)
                name = easygui.multenterbox(
                    "Pose Entries",
                    "2D Pose Entries",
                    ["Poses", "Curves"],
                    [",".join(self.names), line_names],
                )
                if name is not None:
                    if name[0]:
                        self.names = name[0].split(",")
                    if name[1]:
                        self.lines = name[1].split(";")
                        self.lines = [line.split(",") for line in self.lines]

        surface = pg.Surface(window_size, pg.SRCALPHA)
        surface.fill((0,) * 4)
        origin = pose2d_translate(Vector(0, 0))
        pg.draw.rect(
            surface,
            (200, 60, 60),
            (0, origin[1], window_size[0], 1),
        )

        pg.draw.rect(
            surface,
            (60, 200, 60),
            (origin[0], 0, 1, window_size[1]),
        )

        for name in self.names:
            x_entry = float(table[f"{name}.x"]["value"])
            y_entry = float(table[f"{name}.y"]["value"])
            angle_entry = float(table[f"{name}.angle"]["value"])
            position = Vector(x_entry, y_entry)
            new_corners = [
                position + Rotation2d(angle_entry).rotate(point * 0.5)
                for point in Pose2dView.square
            ]
            pg.draw.polygon(
                surface,
                (60, 60, 200),
                [
                    pose2d_translate(new_corners[0]),
                    pose2d_translate(new_corners[1]),
                    pose2d_translate(new_corners[2]),
                ],
            )
            pg.draw.polygon(
                surface,
                (60, 60, 200),
                [
                    pose2d_translate(new_corners[0]),
                    pose2d_translate(new_corners[3]),
                    pose2d_translate(new_corners[2]),
                ],
            )
            pg.draw.line(
                surface,
                (60, 200, 60),
                pose2d_translate(position),
                pose2d_translate(
                    position + Rotation2d(angle_entry).rotate(Vector(1, 0))
                ),
                1,
            )

            surface.blit(self.font.render(name), pose2d_translate(position))

        for line in self.lines:
            curve_points = []
            for name in line:
                x_entry = float(table[f"{name}.x"]["value"])
                y_entry = float(table[f"{name}.y"]["value"])
                curve_points.append(Vector(x_entry, y_entry))

            if curve_points:
                curve = BezierCurve(curve_points)
                prev_point = pose2d_translate(curve.get_point(0))
                for i in range(1, 51):
                    pt = pose2d_translate(curve.get_point(i / 50))
                    pg.draw.line(
                        surface,
                        (200, 60, 200),
                        prev_point,
                        pt,
                    )
                    prev_point = pt
        return surface
