from threading import Thread
from robot import Robot
from flask import Flask
import sys
from time import sleep
import json

bot = Robot()
app = Flask(__name__)


def bot_main():
    while True:
        bot.run()
        sleep(0.05)


@app.route('/')
def root():
    return ''


@app.route('/up_start')
def up_start():
    bot.trigger_start('up')
    return ''


@app.route('/up_end')
def up_end():
    bot.trigger_end('up')
    return ''


@app.route('/down_start')
def down_start():
    bot.trigger_start('down')
    return ''


@app.route('/down_end')
def down_end():
    bot.trigger_end('down')
    return ''


@app.route('/left_start')
def left_start():
    bot.trigger_start('left')
    return ''


@app.route('/left_end')
def left_end():
    bot.trigger_end('left')
    return ''


@app.route('/right_start')
def right_start():
    bot.trigger_start('right')
    return ''


@app.route('/right_end')
def right_end():
    bot.trigger_end('right')
    return ''


@app.route('/action_start')
def action_start():
    bot.trigger_start('action')
    return ''


@app.route('/action_end')
def action_end():
    bot.trigger_end('action')
    return ''


@app.route('/get_data')
def get_data():
    return json.dumps(bot.get_data)


if __name__ == '__main__':
    robot_thread = Thread(target=bot_main)
    robot_thread.start()
    app.run(host=sys.argv[1], port=sys.argv[2])
