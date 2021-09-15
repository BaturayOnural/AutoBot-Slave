from flask import Flask, send_from_directory, redirect
from flask import request
from random import randrange
import requests
import os
from selenium import webdriver
import time


# Api keys
webshare_api_key = "3c43d9fc51d65c8cf7fe3bb85d1ecfcade8b41be"

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# globals
IP = ""
PORT = ""
PROXY = IP + ":" + PORT
status = "0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
#chrome = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

#chrome.get("https://www.google.com/search?channel=fs&client=ubuntu&q=what+is+my+ip+address")


# Casual routes for pages
@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/get_status')
def get_status():
    return status

@app.route('/email')
def hello():
    global IP, PORT, PROXY, status
    IP = ""
    PORT = ""
    PROXY = IP + ":" + PORT
    status = "1"
    time.sleep(7)
    status="2"
    time.sleep(7)
    status="3"
    return "Email Generated!"

# Run server from terminal
if __name__ ==  "__main__":
    app.run(host="0.0.0.0")
