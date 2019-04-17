from flask import Flask, render_template
from hex2dec2bin import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/hex-dec-bin')
def hex2dec2bin():
    return render_template('hex2dec2bin.html')


@app.route('/rubik')
def rubick():
    return render_template('rubik.html')


@app.route('/divisas')
def divisa():
    return render_template('divisas.html')


@app.route('/upm-menu')
def menuUpm():
    return render_template('upmMenu.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)