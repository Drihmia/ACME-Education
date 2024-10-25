#!/usr/bin/python3
"""This module verify if user's email is valid and fonctionnal"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from flask import jsonify, request, redirect, render_template, url_for
from itsdangerous import URLSafeTimedSerializer
from json import dumps, loads
from os import getenv
from werkzeug.exceptions import BadRequest
from datetime import datetime as date
from api.v1.views import app_views
from tools.send_email import send_emails, generate_verification_email


load_dotenv()
current_datetime = date.now().strftime("%B %d, %Y at %I:%M %p")

# Serializer for generating and validating tokens
secret_key = getenv('SECRET_KEY')
if not secret_key:
    print("secret key, for serializer, is none")
    exit(1)

serializer = URLSafeTimedSerializer(secret_key)

FRONT_END_ROUTER = getenv('FRONT_END_ROUTER')
if FRONT_END_ROUTER:
    FRONT_END_ROUTER = FRONT_END_ROUTER

BACK_END_ROUTER = getenv('BACK_END_ROUTER')
if BACK_END_ROUTER:
    BACK_END_ROUTER = BACK_END_ROUTER


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

    print("send verification mail for:", data)
    print("time:", current_datetime)
    if 'email' not in data.keys():
        return jsonify({'error': 'Missing email for verification \
for sending verification email'}), 400

    if 'is_teacher' not in data.keys():
        return jsonify({'error': 'Missing is_teacher'}), 400

    EMAIL_SEND = getenv('ACME_EMAIL')
    if not EMAIL_SEND:
        return jsonify(error='export ACME_EMAIL="Your_email@gmail.com" \
into ur bashrc file')

    # All the sent data is going to be stored in this token
    # +and verified by next method down bellow.
    token = serializer.dumps(data)

    login = getenv('DRIHMIA_EMAIL')

    try:
        # --------------------- SEND VERIFICATION EMAIL ----------------------
        # --------------------------------------------------------------------
        is_teacher = data.get('is_teacher')
        user = 'Teacher' if is_teacher is True else 'Student'
        verific_link = f"{BACK_END_ROUTER}/api/v1/verify_email_recieve/{token}?teacher={is_teacher}"

        body = generate_verification_email(user, verific_link, login)

        # --------------------- SEND VERIFICATION EMAIL ----------------------
        # --------------------------------------------------------------------
        error = send_emails([data.get('email')], 'Please Verify Your Email', body)
        if error:
            print('e1:', error)
            return jsonify({ 'error': 'INVALID EMAIL', 'details': error }), 400

    except Exception as e:
        print('e2:', e)
        return jsonify({
            'status': 'SEND VERIFICATION MAIL FAILED, Check credentials'
        }), 400

    return jsonify({'status': 'SEND VERIFICATION MAIL SUCCEEDED'}), 200


@app_views.route("/verify_email_recieve/<token>", methods=["GET"],
                 strict_slashes=False)
def verify_email_recieve(token):
    """
    A function that verify the token based on the SECRET_KEY.
    """
    is_teacher = request.args.get('teacher')

    try:
        data = serializer.loads(token, max_age=3600)
        print("recieved Registration from:", data)
        print("time:", current_datetime)
    except Exception:
        return redirect(url_for('app_views.token_error', is_teacher=is_teacher), code=301)
        # return jsonify({'status': 'VERIFICATION FAILS'}), 400

    if 'is_teacher' not in data.keys():
        return jsonify({
            'error': 'Missing is_teacher during verification'}), 400

    import requests
    url = f"{BACK_END_ROUTER}/api/v1/"
    headers = {'Content-Type': 'application/json'}

    if data.get('is_teacher') is True:
        # Making a POST request with a with context manager
        base = 'teachers'
        url = url + base
        with requests.post(url, data=dumps(data), headers=headers) as res:
            if res.status_code == 201:
                try:
                    with requests.get(FRONT_END_ROUTER) as res:
                        if res.status_code == 200:
                            return redirect(
                                url_for('app_views.confirmation', is_teacher=is_teacher), code=301)
                        raise requests.exceptions.ConnectionError
                except requests.exceptions.ConnectionError:
                    return jsonify({'status': "EMAIL VERIFIED AND \
TEACHER's PROFILE CREATED"}), 201
            else:
                # If status code is 700 means teacher's email already in
                # +our database and it will be redirect to login page.
                if res.status_code == 700:
                    try:
                        with requests.get(FRONT_END_ROUTER) as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.already_exists', is_teacher=is_teacher),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            loads(res.text)), int(res.status_code)
                elif res.status_code == 409:
                    try:
                        with requests.get(FRONT_END_ROUTER) as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.conflict_teacher', is_teacher=is_teacher),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            loads(res.text)), int(res.status_code)
                return jsonify(
                    loads(res.text)), int(res.status_code)
    else:
        base = 'students'
        url = url + base
        with requests.post(url, data=dumps(data), headers=headers) as res:
            if res.status_code == 201:
                try:
                    with requests.get(FRONT_END_ROUTER) as res:
                        if res.status_code == 200:
                            return redirect(
                                url_for('app_views.confirmation', is_teacher=is_teacher), code=301)
                        raise requests.exceptions.ConnectionError
                except requests.exceptions.ConnectionError:
                    return jsonify({'status': "EMAIL VERIFIED AND \
STUDENT's PROFILE CREATED"}), 201
            else:
                # If status code is 700 means student's email already in
                # +our database and it will be redirect to login page.
                if res.status_code == 700:
                    try:
                        with requests.get(FRONT_END_ROUTER) as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.already_exists', is_teacher=is_teacher),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            loads(res.text)), int(res.status_code)
                elif res.status_code == 409:
                    try:
                        with requests.get(FRONT_END_ROUTER) as res:
                            if res.status_code == 200:
                                return redirect(
                                    url_for('app_views.conflict_student', is_teacher=is_teacher),
                                    code=301)
                            raise requests.exceptions.ConnectionError
                    except requests.exceptions.ConnectionError:
                        return jsonify(
                            loads(res.text)), int(res.status_code)
                return jsonify(
                    loads(res.text)), int(res.status_code)


@app_views.route('/confirmation')
def confirmation():
    """A function that render the confirmation template.
    """
    is_teacher = request.args.get("is_teacher", '')
    print("confirmation")
    print("time:", current_datetime)

    url = f"{FRONT_END_ROUTER}/login?msg=success_registration"
    info = 'Registration Successful'
    message = f"""Registration Confirmed! Your{is_true(is_teacher, " Teacher's", " Student's", '')} account has
    been successfully created."""
    login = f'   Login{is_true(is_teacher, " Teacher", " Student", '')} '
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/already_exists')
def already_exists():
    """
    A function that render the already exists template.
    """
    print("already_exists")
    print("time:", current_datetime)
    url = f"{FRONT_END_ROUTER}/login"
    info = 'Account Already Exists'
    message = """An account with this email address already exists.<br>
    <small>Would you like to log in instead?</small>"""
    login = '   Login  '
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/conflict_student')
def conflict_student():
    """A function that render the already exists template in case of conflict.
    """
    print("conflict_student")
    print("time:", current_datetime)
    url = f"{FRONT_END_ROUTER}/login"
    info = 'Account Already Exists As Teacher'
    message = """This email is already registered as a Teacher.\
        <br><small>Cannot sign up as a Student</small>"""
    login = 'Login As Teacher'
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/conflict_teacher')
def conflict_teacher():
    """ a function that render the confirmation template"""
    print("conflict_teacher")
    print("time:", current_datetime)
    url = f"{FRONT_END_ROUTER}/login"
    info = 'Account Already Exists As Student'
    message = """This email is already registered as a Student.\
    <br> <small>cannot sign up as Teacher</small>"""
    login = 'Login As Student '
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)


@app_views.route('/token_error')
def token_error():
    """A function that renders the token error template."""
    print("token_error")
    print("time:", current_datetime)
    is_teacher = request.args.get('is_teacher', '')

    # Adjust the sign-up URL based on whether the user is a teacher or student
    url = f"{FRONT_END_ROUTER}/signup" + is_true(is_teacher, "/teacher", "/student", '')
    info = 'Error occurred during email verification'

    email_address = getenv('DRIHMIA_EMAIL')
    subject = "Token has expired or Not copied correctly"
    body = """Describe Your Issue Here:
    %0A- ...
    %0A- ....
    %0A- ...."""

    mailto_link = f'mailto:{email_address}?subject={subject}&body={body}'
    message = f"""<br>
    Please copy and paste the verification link correctly or use the
    'Verify Your Account' button.<br>
    <small>If the issue persists, please <a href="{mailto_link}">contact us</small>"""

    login = 'Sign up' + is_true(is_teacher, ' as a Teacher', ' as a Student', '')
    return render_template('confirme_registration.html', url=url,
                           info=info, message=message, login=login)

def is_true(value: str, option1: str, option2: str, option3: str):
    """ evaluate the value
    return:
     - option1 is value is true.
     - option2 if value is false.
     - option3 if value is something else, not boolen.
    """

    if value.lower() == 'true':
        return option1
    elif value.lower() == 'false':
        return option2
    else:
        return option3
