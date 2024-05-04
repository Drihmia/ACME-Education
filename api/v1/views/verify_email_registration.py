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
        return jsonify({'error': 'Missing email for verification'}), 400

    token = serializer.dumps(data)

    # Initialize Yagmail with the OAuth2 credentials
    yag = yagmail.SMTP('newonerad@gmail.com', oauth2_file='~/oauth2_creds.json')

    # Send a test email
    yag.send(
        to=data.get('email'),
        subject='Verification',
        contents=f'http://127.0.0.1:5000/api/v1/verify_email_recieve/{token}'
    )
    # print("************************************************")
    # print("data send", data)
    # print("token:", token)
    # print("************************************************")

    return jsonify({'status': 'OK'}), 200
