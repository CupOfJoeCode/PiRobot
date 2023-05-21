import pygame as pg
import sys
from font import Font
import requests
import json
import easygui
from views import TableView, Pose2dView


def main():
    SERVER = "192.168.5.1"
    PORT = "58012"

    if ("-h" in sys.argv) or ("--help" in sys.argv):
        print(
            "Options: \n-h, --help: Show this menu\n-i <IP>: specify the IP Address\n-p <PORT>: specify the port"
        )
        return

    server_flag = False
    port_flag = False
    for arg in sys.argv:
        if server_flag:
            SERVER = arg
            server_flag = False
        elif port_flag:
            PORT = arg
            port_flag = False
        else:
            if arg.startswith("-i"):
                server_flag = True
            elif arg.startswith("-p"):
                port_flag = True

    URL = f"http://{SERVER}:{PORT}"

    print(URL)
    pg.init()
    pg.display.set_caption("PiRobot Control")
    pg.display.set_icon(pg.image.load("icon.png"))
    d = pg.display.set_mode((800, 600), pg.RESIZABLE)
    font = Font()

    table_view = TableView(font, URL)
    pose2d_view = Pose2dView(font)

    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        rel_x, rel_y = pg.mouse.get_rel()
        mouses = pg.mouse.get_pressed()
        mouse_down = mouses[0]
        mouse_right = mouses[2]
        scroll_dir = 0
        TRIGGERS = {
            pg.K_UP: "up",
            pg.K_DOWN: "down",
            pg.K_LEFT: "left",
            pg.K_RIGHT: "right",
        }

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
                elif e.key in TRIGGERS:
                    requests.get(f"{URL}/trigger_start?trigger={TRIGGERS[e.key]}")
            elif e.type == pg.KEYUP:
                if e.key in TRIGGERS:
                    requests.get(f"{URL}/trigger_end?trigger={TRIGGERS[e.key]}")
            elif e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 4:
                    scroll_dir = -1
                elif e.button == 5:
                    scroll_dir = 1

        table = json.loads(requests.get(f"{URL}/get_data").text)

        d.fill((60,) * 3)
        window_size = (d.get_width() // 2, (d.get_height() - 32) // 2)

        d.blit(
            table_view.update(
                table,
                (mouse_x, mouse_y - 32),
                (rel_x, rel_y),
                mouse_down,
                mouse_right,
                scroll_dir,
                window_size,
            ),
            (0, 32),
        )

        d.blit(
            pose2d_view.update(
                table,
                (mouse_x, mouse_y - 32 - window_size[1]),
                (rel_x, rel_y),
                mouse_down,
                mouse_right,
                scroll_dir,
                window_size,
            ),
            (0, 32 + window_size[1]),
        )

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
