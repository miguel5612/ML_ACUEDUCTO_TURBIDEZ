# app.py
"""Flask App Project."""

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from sklearn.externals import joblib
import numpy as np
#import argparse
#import imutils
#import cv2


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/dash', methods=['GET'])
def dashboard():
    return render_template('dash.html')

@app.route('/l', methods=['GET'])
def lol():
    return "lol"

@app.route('/favicon.ico')
def favicon():
    return 'no hay'

if __name__ == '__main__':
    app.run()