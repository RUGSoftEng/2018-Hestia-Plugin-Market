# This represents the backend server that handles all of the routing requests
# made from the webgui to the local hestia controllers
# SQL Alchemy manages Database

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

# Timeout for requests.

TIMEOUT = 1.00

# Create endpoints


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/devices.html')
def devices():
    return render_template('devices.html')


@app.route('/server.html')
def server():
    return render_template('server.html')


@app.route('/settings.html')
def settings():
    return render_template('settings.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/request', methods=['POST'])
def apiRequestHandler():
    json = request.get_json()
    url = json["query"]
    method = json["method"]
    payload = None
    if ("payload" in json):
        payload = json["payload"]
        if ("state" in payload and "type" in payload):
            if (payload["type"] == "float"):
                payload["state"] /= 1.0
    return routeRequest(method, url, payload)


# Handle routing requests according to rest principles

def routeRequest(method, query, payload):
    result = ""
    print("Sending request to server:", method, ", ", query, ", ", payload)
    if (method == "GET"):
        result = requests.get(query,
                              verify=False,
                              timeout=TIMEOUT).text
    elif (method == "POST"):
        result = requests.post(query,
                               verify=False,
                               json=payload,
                               timeout=TIMEOUT).text
    elif (method == "PUT"):
        result = requests.put(query,
                              verify=False,
                              json=payload,
                              timeout=TIMEOUT).text
    elif (method == "DELETE"):
        result = requests.delete(query,
                                 verify=False,
                                 timeout=TIMEOUT).text
    else:
        result = "Invalid REST method."
    return result
