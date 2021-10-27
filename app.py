from flask import Flask, send_from_directory, redirect
from flask import request
from random import randrange
from flask_cors import CORS
import requests
import os
from selenium import webdriver
import time

webshare_api_key = "3c43d9fc51d65c8cf7fe3bb85d1ecfcade8b41be"
status="0"

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

@app.route('/email/<str:proxy>/<str:name>/<str:surname>')
def email(proxy, name, surname):
    global status
    status = "0"

    response = requests.get("https://proxy.webshare.io/api/proxy/list/", headers={"Authorization": webshare_api_key})
    response = response.json()

    response = response.get("results")[0]
    IP = str(response.get("proxy_address"))
    PORT = str(response.get("ports").get("http"))
    PROXY = IP + ":" + PORT

    NAME = "Hasan"
    SURNAME = "KALYONCU"

    os.system("python yandex_registration.py " + PROXY + " " + NAME + " " + SURNAME)

    return "Email Generated!"

# Run server from terminal
if __name__ ==  "__main__":
    app.run(host="0.0.0.0")
