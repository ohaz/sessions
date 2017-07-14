from app import app, basepath
from flask import render_template, abort, request
from session import Session
import json
import os


@app.route('/')
def index():
    sessions = [Session(title="Test", author="TestAuthor")]
    return render_template('index.html', sessions=sessions)
