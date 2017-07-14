import os

from flask import Flask

__author__ = 'ohaz'

app = Flask(__name__)


basepath = os.path.dirname(os.path.realpath(__file__))

debug = True
host = '0.0.0.0'
port = 7352
