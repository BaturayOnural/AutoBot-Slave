from flask import Flask, render_template, send_from_directory, jsonify, redirect
from flask import request
from random import randrange
import requests
import os

# Api keys
webshare_api_key = "3c43d9fc51d65c8cf7fe3bb85d1ecfcade8b41be"

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Casual routes for pages
@app.route('/hello')
def overview():
    return "Hello World!"

# Run server from terminal
if __name__ ==  "__main__":
    app.run(debug=True)
