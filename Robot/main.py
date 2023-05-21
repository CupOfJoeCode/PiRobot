import json
import logging
import sys
from threading import Thread
from time import sleep

from flask import Flask, request

from robot import Robot
from pibot.base.datatable import EntryType

bot = Robot()
app = Flask(__name__)

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


def bot_main():
    while bot.running:
        bot.run()
        bot.data.put_boolean("Stopped", False)
        sleep(0.05)
    bot.stop()
    bot.data.put_boolean("Stopped", True)


@app.route("/")
def root():
    return ""


@app.route("/trigger_start")
def trigger_start():
    bot.trigger_start(request.args.get("trigger"))
    return ""


@app.route("/trigger_end")
def trigger_end():
    bot.trigger_end(request.args.get("trigger"))
    return ""


@app.route("/get_data")
def get_data():
    out_dict = {}
    for key in bot.data.entries:
        entry = bot.data.entries[key]
        out_dict[key] = {"type": entry.entry_type, "value": entry.value}
    return json.dumps(out_dict)


@app.route("/set_data")
def set_data():
    key = request.args.get("key")
    entry_type = int(request.args.get("type"))
    val = request.args.get("value")

    if entry_type in range(3):
        if entry_type == EntryType.NUMBER:
            bot.data.put_number(key, float(val))
        elif entry_type == EntryType.BOOL:
            bot.data.put_boolean(key, val == "1")
        elif entry_type == EntryType.TEXT:
            bot.data.put_text(key, val)

    return ""


@app.route("/set_color")
def set_color():
    red = int(request.args.get("red"))
    green = int(request.args.get("green"))
    blue = int(request.args.get("blue"))
    threshold = int(request.args.get("threshold"))
    bot.vision.set_target_color(red, green, blue, threshold)
    return ""


@app.route("/stop")
def stop():
    bot.running = False
    return ""


@app.route("/start")
def start():
    if not bot.running:
        bot.running = True
        robot_thread = Thread(target=bot_main)
        robot_thread.start()
    return ""


if __name__ == "__main__":
    port = "58012"
    for arg in sys.argv:
        if arg.startswith("-p"):
            port = arg[2:]

    bot.data.put_boolean("Stopped", True)
    app.run(host="0.0.0.0", port=port, debug=False)
