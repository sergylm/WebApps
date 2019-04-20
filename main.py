from flask import Flask, render_template, request, jsonify
from hex2dec2bin import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/hex-dec-bin')
def hex2dec2bin():
    return render_template('hex2dec2bin.html')


""""@app.route('/hex-dec-bin/api/hex', methods=['GET'])
def h2d2bapi():
    if not request.method == 'GET':
        return 'error'
    else:
        num = request.form['hex1']
        return [{'hex': num, 'dec': bin2dec(hex2bin(num)), 'bin': hex2bin(num)}]
"""
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