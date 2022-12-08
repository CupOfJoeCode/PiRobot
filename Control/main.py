import base64
import pygame as pg
import requests
import sys
import json
from widget import DataWidget
import easygui
import pygame.gfxdraw


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
    pg.display.set_icon(pg.image.load('icon.png'))
    d = pg.display.set_mode((800, 600))
    ip = sys.argv[1]
    port = sys.argv[2]
    server = f'http://{ip}:{port}/'

    camera = pg.Surface((128, 128))
    camera.fill((60, 200, 60))
    frame_count = 0
    camera_x = d.get_width() - 256
    camera_y = d.get_height() - 256
    while True:
        clicked = False
        for e in pg.event.get():
            if e.type == pg.QUIT:
                requests.get(f'{server}stop')
                pg.quit()
                quit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_RETURN:
                    requests.get(f'{server}stop')
                elif e.key == pg.K_BACKSLASH:
                    requests.get(f'{server}start')
                elif e.key in key_codes:
                    requests.get(
                        f'{server}trigger_start?trigger={key_codes[e.key]}')

            elif e.type == pg.KEYUP:
                if e.key in key_codes:
                    requests.get(
                        f'{server}trigger_end?trigger={key_codes[e.key]}')

            elif e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1:
                    clicked = True
        robot_data = json.loads(requests.get(f'{server}get_data').text)
        camera_target = requests.get(f'{server}get_target').text
        if camera_target:
            camera_target = json.loads(camera_target)
        else:
            camera_target = None
        mouse_x, mouse_y = pg.mouse.get_pos()
        d.fill((0, 0, 0))
        d.blit(pg.transform.scale(camera, (256, 256)), (camera_x, camera_y))
        if camera_target is not None:
            target_x = int((camera_target['x']*0.5+0.5)*256)
            target_y = int((camera_target['y']*0.5+0.5)*256)
            target_radius = int(camera_target['radius']*512)
            pg.draw.circle(d, (0, 255, 0), (target_x +
                           camera_x, target_y+camera_y), target_radius, 2)
        x_pos = 0
        y_pos = 0

        for key in robot_data:
            widget = DataWidget()
            widget.set_title(key)
            widget.set_value(robot_data[key])

            widget_x = x_pos*140+10
            widget_y = y_pos*140+10

            d.blit(widget.get_surface(), (widget_x, widget_y))

            if clicked:
                if mouse_x in range(widget_x, widget_x + 128):
                    if mouse_y in range(widget_y, widget_y + 128):
                        if widget.isbool:
                            requests.get(
                                f'{server}set_data?key={key}&value={not robot_data[key]}')
                        else:
                            new_val = easygui.enterbox(
                                key, "Set Value", robot_data[key])
                            if new_val is not None:
                                requests.get(
                                    f'{server}set_data?key={key}&value={new_val}')

            x_pos += 1
            if x_pos > 5:
                x_pos = 0
                y_pos += 1

        if clicked:
            if mouse_x in range(camera_x, d.get_width()):
                if mouse_y in range(camera_y, d.get_height()):
                    pixel_x = (mouse_x - camera_x)//2
                    pixel_y = (mouse_y - camera_y)//2
                    clr = camera.get_at((pixel_x, pixel_y))
                    new_val = easygui.enterbox(
                        "Set Threshold", "Set Threshold", 30)
                    if new_val is not None:
                        if new_val.isdigit():
                            requests.get(
                                f'{server}set_color?red={clr[0]}&green={clr[1]}&blue={clr[2]}&threshold={new_val}')

        frame_count += 1
        if(frame_count > 30):
            data = requests.get(f'{server}camera').text
            if data:
                data = base64.b16decode(data)
                camera = pg.image.frombuffer(data, (128, 128), 'RGB')
            frame_count = 0

        pg.display.update()
        pg.time.wait(1)


if __name__ == '__main__':
    main()
