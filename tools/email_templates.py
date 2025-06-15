updated_html_verifivation_email = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #F0F9FF;
            line-height: 1.6;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .link-container {
            text-align: center;
            margin: 20px 0;
        }
        .footer {
            margin-top: 30px;
            font-size: 12px;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <p>Dear {user},</p>
        <p>Thank you for registering with <strong>ACME EDUCATION</strong>!</p>
        <p><strong>Date and Time:</strong> {current_datetime}</p>
        <p>To complete your registration, please verify your email address by clicking the button below:</p>
        <div class="link-container">
            <a href="{verific_link}" class="button">Verify Your Account</a>
        </div>
        <p>If you're unable to click the button, you can copy and paste the following link into your browser:</p>
        <p><a href="{verific_link}">{verific_link}</a></p>
        <p>By verifying your email address, you'll gain access to all the features of ACME EDUCATION.</p>
        <p>If you did not register for an account with ACME EDUCATION, please ignore this email or contact us immediately at <a href="mailto:{contact_email}">ACME EDUCATION</a> to report any unauthorized activity.</p>
        <p>Thank you for choosing <strong>ACME EDUCATION</strong>!</p>
        <p>Best regards,<br>The ACME EDUCATION Team</p>
        <div class="footer">
            <p><strong>ACME EDUCATION</strong><br>
            <a href="mailto:{contact_email}">{contact_email}</a></p>
        </div>
    </div>
</body>
</html>
"""

updated_html_lesson_notification = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #F0F9FF;
            line-height: 1.6;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .footer {
            margin-top: 30px;
            font-size: 12px;
            color: #777;
        }
        .lesson-info {
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
            background-color: #fff;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <p>Dear {student_name},</p>
        <p>A new lesson has been released! Please log in to your account on <strong>ACME EDUCATION</strong> to check the details.</p>
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
        <p>If you have any questions or need further assistance, feel free to reach out to your teacher or contact us at <a href="mailto:{contact_email}">ACME EDUCATION</a>.</p>
        <p>Happy learning!</p>
        <p>Best regards,<br>The ACME EDUCATION Team</p>
        <div class="footer">
            <p><strong>ACME EDUCATION</strong><br>
            <a href="mailto:{contact_email}">{contact_email}</a></p>
        </div>
    </div>
</body>
</html>
"""

plain_text_verifivation_email = """
Dear {user},

Thank you for registering with ACME EDUCATION!

Date and Time: {current_datetime}

To complete your registration, please verify your email address by clicking the link below:
{verific_link}

If you're unable to click the link, you can copy and paste the following link into your browser:
{verific_link}

By verifying your email address, you'll gain access to all the features of ACME EDUCATION.

If you did not register for an account with ACME EDUCATION, please ignore this email or contact us immediately at {contact_email}.

Thank you for choosing ACME EDUCATION!

Best regards,
The ACME EDUCATION Team

Contact Us: {contact_email}
"""

plain_text_lesson_notification = """
Dear {user},

Thank you for registering with ACME EDUCATION!

Date and Time: {current_datetime}

To complete your registration, please verify your email address by clicking the link below:
{verific_link}

If you're unable to click the link, you can copy and paste the following link into your browser:
{verific_link}

By verifying your email address, you'll gain access to all the features of ACME EDUCATION.

If you did not register for an account with ACME EDUCATION, please ignore this email or contact us immediately at {contact_email}.

Thank you for choosing ACME EDUCATION!

Best regards,
The ACME EDUCATION Team

Contact Us: {contact_email}
"""
