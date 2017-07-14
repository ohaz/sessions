from flask import render_template, abort, request
from session import Session
import json
import os
from app import app, basepath

origin = None


@app.route('/')
def index():
    if not os.path.exists(os.path.join('git', 'sessionsTest', 'sessions.json')):
        abort(404)
    jsonl = None
    with open(os.path.join('git', 'sessionsTest', 'sessions.json')) as f:
        jsonl = json.load(f)
    sessions = [Session(title=x['title'], author=x['author']) for x in jsonl['sessions']]
    return render_template('index.html', sessions=sessions)


@app.route('/github/', methods=['GET', 'POST'])
def github():
    jsonl = json.loads(request.data.decode('utf-8'))
    try:
        if jsonl['action'] == "closed":
            if "pull_request" in jsonl:
                origin.pull()
        return "OK"
    except:
        abort(500)