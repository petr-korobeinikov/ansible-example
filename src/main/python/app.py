from flask import Flask
from flask import render_template
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


@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    t = render_template('user.j2', username=username)
    return t

if __name__ == "__main__":
    app.run(host='0.0.0.0')
