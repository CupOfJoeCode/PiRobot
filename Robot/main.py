from threading import Thread
from robot import Robot
from flask import Flask, request
import sys
from time import sleep
import json

bot = Robot()
app = Flask(__name__)


def bot_main():
    while bot.running:
        bot.run()
        sleep(0.05)
    bot.stop()


@app.route('/')
def root():
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
    return json.dumps(bot.get_data())


@app.route('/stop')
def stop():
    bot.running = False
    return ''


if __name__ == '__main__':
    robot_thread = Thread(target=bot_main)
    robot_thread.start()
    app.run(host=sys.argv[1], port=sys.argv[2], debug=False)
