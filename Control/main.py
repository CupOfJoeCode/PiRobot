from random import randint
import pygame as pg
import requests
import sys
import json


def main():

    key_codes = {
        pg.K_UP: 'up',
        pg.K_DOWN: 'down',
        pg.K_LEFT: 'left',
        pg.K_RIGHT: 'right',
        pg.K_SPACE: 'action'
    }

    pg.init()
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
                if e.key in key_codes:
                    requests.get(f'{server}{key_codes[e.key]}_start')
                    d.fill(tuple(map(lambda _: randint(0, 255), [0]*3)))
            elif e.type == pg.KEYUP:
                if e.key in key_codes:
                    requests.get(f'{server}{key_codes[e.key]}_end')
                    d.fill(tuple(map(lambda _: randint(0, 255), [0]*3)))

        robot_data = json.loads(requests.get(f'{server}get_data').text)

        pg.display.update()


if __name__ == '__main__':
    main()
