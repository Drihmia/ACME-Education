#!/usr/bin/python3
"""This module verify if user's email is valid and fonctionnal"""

from flask import jsonify, request, redirect, url_for
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
    except Exception:
        return jsonify({'status': 'SEND VERIFICATION MAIL FAILED'}), 400

    return jsonify({'status': 'SEND VERIFICATION MAIL SUCCEEDED'}), 200


@app_views.route("/verify_email_recieve/<token>", methods=["GET"],
                 strict_slashes=False)
def verify_email_recieve(token):
    try:
        data = serializer.loads(token, max_age=3600)
    except Exception:
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
        url = url + base
        with requests.post(url, data=json.dumps(data), headers=headers) as res:
            if res.status_code == 201:
                with requests.get('http://127.0.0.1:3000') as res:
                    if res.status_code == 200:
                        url_s = 'http://127.0.0.1:3000'
                        base = '/login?msg=success_registration'
                        return redirect(url_s + base, code=301)
                    else:
                        return jsonify({'status': "EMAIL VERIFIED AND \
TEACHER's PROFILE CREATED"}), 201
            else:
                return jsonify(json.loads(res.text)), int(res.status_code)
    else:
        base = 'students'
        url = url + base
        with requests.post(url, data=json.dumps(data), headers=headers) as res:
            if res.status_code == 201:
                with requests.get('http://127.0.0.1:3000') as res:
                    if res.status_code == 200:
                        url_s = 'http://127.0.0.1:3000'
                        base = '/login?msg=success_registration'
                        return redirect(url_s + base, code=301)
                    else:
                        return jsonify({'status': "EMAIL VERIFIED AND \
STUDENT's PROFILE CREATED"}), 201
            else:
                return jsonify(
                    json.loads(res.text)), int(res.status_code)


