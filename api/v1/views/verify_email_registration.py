#!/usr/bin/python3
"""This module verify if user's email is valid and fonctionnal"""

from flask import jsonify, request, redirect, render_template, url_for
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

    if 'is_teacher' not in data.keys():
        return jsonify({'error': 'Missing is_teacher'}), 400

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
                try:
                    with requests.get('http://127.0.0.1:3000') as res:
                        print(res.status_code)
                        if res.status_code == 200:
                            return redirect(
                                url_for('app_views.confirmation'), code=301)
                        raise requests.exceptions.ConnectionError
                except requests.exceptions.ConnectionError:
                    return jsonify({'status': "EMAIL VERIFIED AND \
TEACHER's PROFILE CREATED"}), 201
            else:
                # If status code is 700 means teacher's email already in
                # +our database and it will be redirect to login page.
                if res.status_code == 700:
                    try:
                        with requests.get('http://127.0.0.1:3000') as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.already_exists'),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            json.loads(res.text)), int(res.status_code)
                elif res.status_code == 409:
                    try:
                        with requests.get('http://127.0.0.1:3000') as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.conflict_teacher'),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            json.loads(res.text)), int(res.status_code)
                return jsonify(
                    json.loads(res.text)), int(res.status_code)
    else:
        base = 'students'
        url = url + base
        with requests.post(url, data=json.dumps(data), headers=headers) as res:
            if res.status_code == 201:
                try:
                    with requests.get('http://127.0.0.1:3000') as res:
                        if res.status_code == 200:
                            return redirect(
                                url_for('app_views.confirmation'), code=301)
                        raise requests.exceptions.ConnectionError
                except requests.exceptions.ConnectionError:
                    return jsonify({'status': "EMAIL VERIFIED AND \
STUDENT's PROFILE CREATED"}), 201
            else:
                # If status code is 700 means student's email already in
                # +our database and it will be redirect to login page.
                if res.status_code == 700:
                    try:
                        with requests.get('http://127.0.0.1:3000') as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.already_exists'),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            json.loads(res.text)), int(res.status_code)
                elif res.status_code == 409:
                    try:
                        with requests.get('http://127.0.0.1:3000') as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.conflict_student'),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            json.loads(res.text)), int(res.status_code)
                return jsonify(
                    json.loads(res.text)), int(res.status_code)


@app_views.route('/confirmation')
def confirmation():
    """ a function that render the confirmation template"""
    url = 'http://127.0.0.1:3000/login?msg=success_registration'
    info = 'Registration Successful'
    message = """Registration Confirmed! Your account has
    been successfully created."""
    login = '   Login  '
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/already_exists')
def already_exists():
    """ a function that render the confirmation template"""
    url = 'http://127.0.0.1:3000/login?msg=success_registration'
    info = 'Account Already Exists'
    message = """An account with this email address already exists.
    Would you like to log in instead?"""
    login = '   Login  '
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/conflict_student')
def conflict_student():
    """ a function that render the confirmation template"""
    url = 'http://127.0.0.1:3000/login?msg=success_registration'
    info = 'Account Already Exists As Teacher'
    message = "this email is already registered as a teacher.<br>Cannot sign up as a student"
    login = 'Login As Teacher'
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/conflict_teacher')
def conflict_teacher():
    """ a function that render the confirmation template"""
    url = 'http://127.0.0.1:3000/login?msg=success_registration'
    info = 'Account Already Exists As Student'
    message = """this email is already registered as a student"""
    login = 'Login As Student '
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)
