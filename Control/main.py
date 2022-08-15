import pygame as pg
import requests
import sys
import json
from widget import DataWidget


def main():

    key_codes = {
        pg.K_UP: 'up',
        pg.K_DOWN: 'down',
        pg.K_LEFT: 'left',
        pg.K_RIGHT: 'right',
        pg.K_SPACE: 'action'
    }

    pg.init()
    pg.display.set_caption('PiRobot Controller')
    d = pg.display.set_mode((800, 600))
    ip = sys.argv[1]
    port = sys.argv[2]
    server = f'http://{ip}:{port}/'

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_RETURN:
                    requests.get(f'{server}stop')

                elif e.key in key_codes:
                    requests.get(
                        f'{server}trigger_start?trigger={key_codes[e.key]}')

            elif e.type == pg.KEYUP:
                if e.key in key_codes:
                    requests.get(
                        f'{server}trigger_end?trigger={key_codes[e.key]}')

        robot_data = json.loads(requests.get(f'{server}get_data').text)

        d.fill((0, 0, 0))

        x_pos = 0
        y_pos = 0

        for key in robot_data:
            widget = DataWidget()
            widget.set_title(key)
            widget.set_value(robot_data[key])

            d.blit(widget.get_surface(), (x_pos*140+10, y_pos*140+10))

            x_pos += 1
            if x_pos > 8:
                x_pos = 0
                y_pos += 1

        pg.display.update()


if __name__ == '__main__':
    main()
