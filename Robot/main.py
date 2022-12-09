import base64
import json
import logging
import sys
from threading import Thread
from time import sleep

import cv2
import numpy as np
from flask import Flask, request
from PIL import Image

from robot import Robot

bot = Robot()
app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def bot_main():
    while bot.running:
        bot.run()
        bot.data['Stopped'] = False
        sleep(0.05)
    bot.stop()
    bot.data['Stopped'] = True


@app.route('/')
def root():
    return ''


@app.route('/camera')
def camera():
    if np.any(bot.camera_frame):
        img = cv2.cvtColor(bot.camera_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img).resize((128, 128)).tobytes()
        return base64.b16encode(img)
    return ''


@app.route('/trigger_start')
def trigger_start():
    bot.trigger_start(request.args.get('trigger'))
    return ''


@app.route('/trigger_end')
def trigger_end():
    bot.trigger_end(request.args.get('trigger'))
    return ''


@app.route('/get_data')
def get_data():
    return json.dumps(bot.data)


@app.route('/set_data')
def set_data():
    key = request.args.get('key')
    val = request.args.get('value')
    if val in ['True', 'False']:
        bot.data[key] = val == 'True'
    else:
        try:
            bot.data[key] = float(val)
        except ValueError:
            bot.data[key] = val
    return ''


@app.route('/set_color')
def set_color():
    red = int(request.args.get('red'))
    green = int(request.args.get('green'))
    blue = int(request.args.get('blue'))
    threshold = int(request.args.get('threshold'))
    bot.vision.set_target_color(red, green, blue, threshold)
    return ''


@app.route('/get_target')
def get_target():
    if bot.camera_target is None:
        return ''
    return json.dumps({
        'x': bot.camera_target.x,
        'y': bot.camera_target.y,
        'radius': bot.camera_target.radius
    })


@app.route('/stop')
def stop():
    bot.running = False
    return ''


@app.route('/start')
def start():
    if not bot.running:
        bot.running = True
        robot_thread = Thread(target=bot_main)
        robot_thread.start()
    return ''

if __name__ == '__main__':
    bot.data['Stopped'] = True
    app.run(host=sys.argv[1], port=sys.argv[2], debug=False)
