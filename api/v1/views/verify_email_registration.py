#!/usr/bin/python3
"""This module verify if user's email is valid and fonctionnal"""

from flask import jsonify, request
from itsdangerous import URLSafeTimedSerializer
import json
import os
import yagmail
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views


# Serializer for generating and validating tokens
secret_key = os.environ
if not secret_key:
    print("secret key, for serializer, is none")
    exit(0)
serializer = URLSafeTimedSerializer(secret_key)

@app_views.route("/verify_email_send", methods=["POST"], strict_slashes=False)
def verify_email_send():
    if not request.is_json:
        return jsonify({'error': 'Not a JSON'}), 400

    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({'error': 'Not a JSON'}), 400

    if not data:
        return jsonify({'error': 'No data'}), 422

    if 'email' not in data.keys():
        return jsonify({'error': 'Missing email for verification \
for sending verification email'}), 400

    token = serializer.dumps(data)

    # Initialize Yagmail with the OAuth2 credentials
    yag = yagmail.SMTP('newonerad@gmail.com', oauth2_file='~/oauth2_creds.json')

    # Send a test email
    yag.send(
        to=data.get('email'),
        subject='Verification',
        contents=f'http://127.0.0.1:5000/api/v1/verify_email_recieve/{token}'
    )
    return jsonify({'status': 'OK'}), 200

@app_views.route("/verify_email_recieve/<token>", methods=["GET"], strict_slashes=False)
def verify_email_recieve(token):
    try:
        data = serializer.loads(token, max_age=3600)
    except:
        return jsonify({'status': 'FAIL'}), 400

    if 'is_teacher' not in data.keys():
        return jsonify({'error': 'Missing is_teacher'}), 400

    import requests
    url = 'http://127.0.0.1:5000/api/v1/'
    headers = {'Content-Type': 'application/json'}

    if data.get('is_teacher') == 'True':
        # Making a POST request with a with context manager
        base = 'teachers'
        with requests.post(url + base, data = json.dumps(data), headers=headers) as response:
            if response.status_code == 200:
                return jsonify({'status': 'OK'}), 200
            else:
                return jsonify(json.loads(response.text)), int(response.status_code)
    else:
        base = 'students'
        with requests.post(url + base, data = json.dumps(data), headers=headers) as response:
            if response.status_code == 200:
                return jsonify({'status': 'OK'}), 200
            else:
                return jsonify(json.loads(response.text)), int(response.status_code)



@app_views.route("/redirect_1", methods=["GET"], strict_slashes=False)
def redirect_1():

    if request.is_json:
        print('request data from redirect_1')
        print(request.get_json())
        return jsonify({'status': f'ok from redirect_1\n{request.get_json()}'}), 200
    else:
        return jsonify({'error': f'FAIL from redirect_1\n{isinstance(request.args.get("data"), dict)}'}), 400
