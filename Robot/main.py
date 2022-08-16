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
        bot.data['Stopped'] = False
        sleep(0.05)
    bot.stop()
    bot.data['Stopped'] = True


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
    return json.dumps(bot.data)


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


if __name__ == '__main__':
    bot.data['Stopped'] = True
    app.run(host=sys.argv[1], port=sys.argv[2], debug=False)
