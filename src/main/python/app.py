from flask import Flask
import sys
import platform

app = Flask(__name__)


@app.route("/")
def index():
    s = "Hello, I am python '%s' on '%s' machine!\n" % (sys.version, platform.node())
    return s


@app.route("/hello/")
def hello_world():
    hello_world = "Hello World"
    return hello_world


if __name__ == "__main__":
    app.run(host='0.0.0.0')
