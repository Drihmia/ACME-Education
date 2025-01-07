#!/usr/bin/python3
"""
This module contains a function that sends emails using SMTP.
"""
import smtplib
from os import getenv
from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime as date


load_dotenv()


def send_emails(destinations: List[str], subject: str, body: str) -> str | int:
    """
    Send emails using SMTP.

    :param destinations: List of email addresses to send the email to.
    :param subject: Subject of the email.
    :param body: HTML content of the email body.
    """
    smtp_host = getenv('SMTP_HOST')
    smtp_port = int(getenv('SMTP_PORT', 587))
    sender = getenv('DRIHMIA_EMAIL')
    password = getenv('DRIHMIA_PASSWORD')

    # Ensure all required environment variables are set
    if not all([smtp_host, smtp_port, sender, password]):
        raise ValueError("SMTP settings and credentials are required")

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(destinations)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender, password)

        # Send the email
        server.sendmail(msg['From'], destinations, msg.as_string())
        print(f"Email sent successfully to: {', '.join(destinations)}")
        print(f"Subject: {subject}")
        print(f"time: {date.now().strftime("%B %d, %Y at %I:%M %p")}")

        return 0

    except Exception as e:
        print(f"Failed to send email: {e}")
        return str(e)

    finally:
        server.quit()


def generate_verification_email(user: str, verific_link: str, contact_email: str) -> str:
    """
    Generate the HTML email body for account verification.

    Args:
        user (str): The type of user ("Teacher" or "Student").
        verific_link (str): The link for verifying the user's email address.
        contact_email (str): The email address for contact.

    Returns:
        str: The HTML email body as a string.
    """
    current_datetime = date.now().strftime("%B %d, %Y at %I:%M %p")

    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
                --tw-bg-opacity: 1;
                background-color: rgb(240 249 255/var(--tw-bg-opacity));
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                background-color: #007bff;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            }}
            .link-container {{
                text-align: center;
                margin: 20px 0;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <p>Dear {user},</p>

            <p>Thank you for registering with <strong>ACME EDUCATION</strong>!</p>

            <p><strong>Date and Time:</strong> {current_datetime}</p>

            <p>To complete your registration, please verify your email address by clicking the button below:</p>

            <div style="justify-content: space-around; display: flex;">

        <a href="{verific_link}" style="display: inline-block; padding: \
        10px 20px; background-color: #007bff; color: #fff; text-decoration: \
        none; border-radius: 5px; position: absolute;">Verify Your Account</a>

        </div>

            <p>If you're unable to click the button, you can copy and paste the following
            link into your browser:</p>
            <p><a href="{verific_link}">{verific_link}</a></p>

            <p>By verifying your email address, you'll gain access to all the features of
            ACME EDUCATION.</p>

            <p>If you did not register for an account with ACME EDUCATION, please ignore
            this email or contact us immediately at
            <a href="mailto:{contact_email}">ACME EDUCATION</a> to report any unauthorized activity.</p>

            <p>Thank you for choosing <strong>ACME EDUCATION</strong>!</p>

            <p>Best regards,<br>The ACME EDUCATION Team</p>

            <div class="footer">
                <p>strong>ACME EDUCATION</strong><br>
                <a href="mailto:{contact_email}">{contact_email}</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return body


def generate_lesson_notification_email(
    student_name: str,
    teacher_name: str, teacher_email: str,
    lesson_name: str, lesson_description: str, lesson_class: str, lesson_subject: str
) -> str:
    """
    Generate the HTML email body for notifying a student about a new lesson shared by their teacher.

    Args:
        student_name (str): The name of the student.
        teacher_name (str): The name of the teacher.
        teacher_email (str): The email address of the teacher.
        lesson_name (str): The name of the lesson.
        lesson_description (str): A brief description of the lesson.

    Returns:
        str: The HTML email body as a string.
    """
    contact_email = getenv('DRIHMIA_EMAIL')

    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
                --tw-bg-opacity: 1;
                background-color: rgb(240 249 255/var(--tw-bg-opacity));
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #777;
            }}
            .lesson-info {{
                border: 1px solid #ddd;
                padding: 15px;
                border-radius: 5px;
                background-color: #fff;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <p>Dear {student_name},</p>

            <p>A new lesson has been released! Please log in to your account on strong>ACME EDUCATION</strong> to check the details.</p>

            <div class="lesson-info">
                <h3>Lesson Information</h3>
                <p><strong>Lesson Name:</strong> {lesson_name}</p>
                <p><strong>Lesson Class:</strong> {lesson_class}</p>
                <p><strong>Lesson Subject:</strong> {lesson_subject}</p>
                <p><strong>Description:</strong> {lesson_description}</p>
            </div>

            <div class="lesson-info">
                <h3>Teacher Information</h3>
                <p><strong>Name:</strong> {teacher_name}</p>
                <p><strong>Email:</strong> <a href="mailto:{teacher_email}">{teacher_email}</a></p>
            </div>

            <p>If you have any questions or need further assistance, feel free to reach out to your teacher or contact us at
            <a href="mailto:{contact_email}">ACME EDUCATION</a>.</p>

            <p>Happy learning!</p>

            <p>Best regards,<br>The ACME EDUCATION Team</p>

            <div class="footer">
                <p>strong>ACME EDUCATION</strong><br>
                <a href="mailto:{contact_email}">{contact_email}</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return body


if __name__ == "__main__":
    """
    For testing purposes, I may run this module as a script.
    """
    dests = ['newonerad@gmail.com', 'drihmia.redouane@gmail.com']
    sub = 'Testing my function: send_emails'
    content = generate_verification_email('Teacher', 'ref', 're')

    send_emails(dests, sub, content)


