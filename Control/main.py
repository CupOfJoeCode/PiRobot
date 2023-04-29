import pygame as pg
import sys
from font import Font
import requests
import json
import easygui
from vecmath import Vector, Rotation2d, Rotation3d


def main():
    SERVER = sys.argv[1]
    PORT = sys.argv[2]
    URL = f"http://{SERVER}:{PORT}"

    pg.init()
    d = pg.display.set_mode((800, 600), pg.RESIZABLE)
    font = Font()
    pose2d_x = 0
    pose2d_y = 0
    pose2d_ppm = 50

    robot_corners = [
        Vector(-1, -1) * 0.5,
        Vector(1, -1) * 0.5,
        Vector(1, 1) * 0.5,
        Vector(-1, 1) * 0.5,
    ]

    pose2d_name = ""
    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        rel_x, rel_y = pg.mouse.get_rel()
        mouses = pg.mouse.get_pressed()
        mouse_down = mouses[0]
        mouse_right = mouses[2]
        scroll_dir = 0

        for e in pg.event.get():
            if e.type == pg.QUIT:
                requests.get(f"{URL}/stop")
                pg.quit()
                sys.exit(0)
            elif e.type == pg.VIDEORESIZE:
                d = pg.display.set_mode(e.size, pg.RESIZABLE)
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_BACKSLASH:
                    requests.get(f"{URL}/start")
                elif e.key == pg.K_RETURN:
                    requests.get(f"{URL}/stop")
            elif e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 4:
                    scroll_dir = -1
                elif e.button == 5:
                    scroll_dir = 1

        table = json.loads(requests.get(f"{URL}/get_data").text)

        d.fill((60,) * 3)
        window_size = (d.get_width() // 2, (d.get_height() - 32) // 2)

        table_surf = pg.Surface(window_size, pg.SRCALPHA)
        table_surf.fill((0,) * 4)
        pose2d_surf = pg.Surface(window_size, pg.SRCALPHA)
        pose2d_surf.fill((0,) * 4)

        if mouse_x < window_size[0] and mouse_y > 32 + window_size[1]:
            if mouse_down:
                pose2d_x -= rel_x / pose2d_ppm
                pose2d_y += rel_y / pose2d_ppm
            if scroll_dir == 1:
                pose2d_ppm /= 1.1
            elif scroll_dir == -1:
                pose2d_ppm *= 1.1
            if mouse_right:
                name = easygui.enterbox(
                    "Pose Entry Key", "Pose Entry", default=pose2d_name
                )
                if name is not None:
                    pose2d_name = name

        def pose2d_translate(vec):
            screen_x = window_size[0] // 2 - int((pose2d_x - vec.x) * pose2d_ppm)
            screen_y = window_size[1] // 2 + int((pose2d_y - vec.y) * pose2d_ppm)
            return (screen_x, screen_y)

        origin = pose2d_translate(Vector(0, 0))

        pg.draw.rect(
            pose2d_surf,
            (200, 60, 60),
            (0, origin[1], window_size[0], 1),
        )

        pg.draw.rect(
            pose2d_surf,
            (60, 200, 60),
            (origin[0], 0, 1, window_size[1]),
        )

        rot = Rotation2d(0)
        robot_pos = Vector()

        if f"{pose2d_name}.x" in table:
            robot_pos = Vector(
                float(table[f"{pose2d_name}.x"]["value"]),
                float(table[f"{pose2d_name}.y"]["value"]),
            )
            rot = Rotation2d(float(table[f"{pose2d_name}.angle"]["value"]))

        new_corner = [robot_pos + rot.rotate(v) for v in robot_corners]

        pointer = robot_pos + rot.rotate(Vector(1, 0))

        pg.draw.polygon(
            pose2d_surf,
            (60, 60, 200),
            [
                pose2d_translate(new_corner[0]),
                pose2d_translate(new_corner[1]),
                pose2d_translate(new_corner[2]),
            ],
        )

        pg.draw.polygon(
            pose2d_surf,
            (60, 60, 200),
            [
                pose2d_translate(new_corner[3]),
                pose2d_translate(new_corner[2]),
                pose2d_translate(new_corner[0]),
            ],
        )

        pg.draw.line(
            pose2d_surf,
            (60, 200, 60),
            pose2d_translate(robot_pos),
            pose2d_translate(pointer),
            1,
        )

        pose2d_surf.blit(font.render(pose2d_name), (4, 4))

        scr_y = 4
        for key in table:
            entry = table[key]
            if entry["type"] == 0:
                val = float(entry["value"])
                table_surf.blit(font.render(f"{key}: {round(val,2)}"), (4, scr_y))
            elif entry["type"] == 1:
                keysurf = font.render(key)
                val = entry["value"] == "1"
                bg = pg.Surface(keysurf.get_size())
                bg.fill((200, 60, 60) if val else (60, 0, 0))
                bg.blit(keysurf, (0, 0))
                table_surf.blit(bg, (4, scr_y))
            elif entry["type"] == 0:
                val = entry["value"]
                table_surf.blit(font.render(f"{key}: {val}"), (4, scr_y))

            scr_y += 24
        d.blit(table_surf, (0, 32))
        d.blit(pose2d_surf, (0, 32 + window_size[1]))

        pg.draw.rect(d, (0,) * 3, (window_size[0], 32, 1, window_size[1] * 2))
        pg.draw.rect(d, (0,) * 3, (0, window_size[1] + 32, window_size[0] * 2, 1))

        if "Stopped" in table:
            val = table["Stopped"]["value"] == "1"
            pg.draw.rect(
                d, (200, 60, 60) if val else (60, 0, 0), (0, 0, d.get_width(), 32)
            )
            d.blit(font.render("Stopped" if val else "Running"), (8, 8))

        pg.display.update()


if __name__ == "__main__":
    main()
