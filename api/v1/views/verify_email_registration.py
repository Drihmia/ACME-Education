#!/usr/bin/python3
"""This module verify if user's email is valid and fonctionnal"""

from flask import jsonify, request
from itsdangerous import URLSafeTimedSerializer
import json
import os
import yagmail
from yagmail.error import YagInvalidEmailAddress
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views


# Serializer for generating and validating tokens
secret_key = os.environ.get('SECRET_KEY')
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

    EMAIL_SEND = os.environ.get('ACME_EMAIL')
    if not EMAIL_SEND:
        return jsonify(error='export ACME_EMAIL="the_email@gmail.com" \
into ur bashrc file')

    # All the sent data is coing to be stored in this token
    # +and verified by next method down bellow.
    token = serializer.dumps(data)

    try:
        # Initialize Yagmail with the OAuth2 credentials
        yag = yagmail.SMTP(EMAIL_SEND, oauth2_file='~/oauth2_creds.json')

        try:
            # Send a test email
            yag.send(
                to=data.get('email'),
                subject='Verification',
                contents=f'http://127.0.0.1:5000/api/\
v1/verify_email_recieve/{token}'
            )

            # Close connection.
            yag.close()
        except YagInvalidEmailAddress:
            return jsonify({'error': 'INVALID EMAIL'}), 400
    except:
        return jsonify({'status': 'SEND VERIFICATION MAIL FAILED'}), 400

    return jsonify({'status': 'SEND VERIFICATION MAIL SUCCEEDED'}), 200

@app_views.route("/verify_email_recieve/<token>", methods=["GET"],
                 strict_slashes=False)
def verify_email_recieve(token):
    try:
        data = serializer.loads(token, max_age=3600)
    except:
        return jsonify({'status': 'VERIFICATION FAILS'}), 400

    if 'is_teacher' not in data.keys():
        return jsonify({
            'error': 'Missing is_teacher during verification'}), 400

    import requests
    url = 'http://127.0.0.1:5000/api/v1/'
    headers = {'Content-Type': 'application/json'}

    if data.get('is_teacher') == 'True':
        # Making a POST request with a with context manager
        base = 'teachers'
        with requests.post(url + base, data = json.dumps(data), headers=headers) as response:
            if response.status_code == 200:
                return jsonify({'status': 'TEACHER VERIFIED'}), 200
            else:
                return jsonify(json.loads(response.text)), int(response.status_code)
    else:
        base = 'students'
        with requests.post(url + base, data = json.dumps(data), headers=headers) as response:
            if response.status_code == 200:
                return jsonify({'status': 'STUDENT VERIFIED'}), 200
            else:
                return jsonify(json.loads(response.text)), int(response.status_code)
