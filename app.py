from flask import Flask, send_from_directory, redirect
from flask import request
from random import randrange
from flask_cors import CORS
import requests
import os
import time
import signal
import subprocess
import psutil

def kill_child_proc(ppid):
    parent_pid = ppid   # my example
    parent = psutil.Process(parent_pid)
    for child in parent.children(recursive=True):  # or parent.children() for recursive=False
        child.kill()
    parent.kill()

status="0"
pid = 0
task_id = "-1"

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
CORS(app)

# Casual routes for pages
@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/get_status')
def get_status():
    global status
    return status

@app.route('/set_status/<int:stat>')
def set_status(stat):
    global status
    str_vers = str(stat)
    status = str_vers
    return status

@app.route('/email/<proxy>/<task>/<name>/<surname>')
def email(proxy, task, name, surname):
    global status, pid, task_id
    status = "0"
    task_id = task

    PROXY = proxy
    NAME = name
    SURNAME = surname

    command = ["python", "yandex_registration.py", PROXY, NAME, SURNAME, task_id]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    pid = process.pid

    status = "0"

    return "Email Generated!"

@app.route('/kill_email')
def kill_email():
    global status, pid
    kill_child_proc(pid)
    os.kill(pid, signal.SIGKILL)
    status = "0"
    return "Email operation killed!"

@app.route('/git_pull')
def git_pull():
    os.("git pull")
    return "Pulled from github!"

# Run server from terminal
if __name__ ==  "__main__":
    app.run(host="0.0.0.0")
