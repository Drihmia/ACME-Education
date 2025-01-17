from celery import Celery
from tools.send_email import send_emails

# Initialize Celery app with Redis as the broker
app = Celery(
    'acme_education',
    broker='redis://localhost:6379/0',  # Redis URL
    backend='redis://localhost:6379/1',  # Redis result backend
)

@app.task(bind=True, max_retries=3, default_retry_delay=60)  # 3 retries, 60 seconds delay
def send_email_task(self, destinations: list[str], subject: str, body: str):
    """
    Celery task to send emails asynchronously with retry logic.

    :param destinations: List of email addresses to send the email to.
    :param subject: Subject of the email.
    :param body: HTML content of the email body.
    """
    try:
        # Try sending the email
        print("[TASK]: Executing queued tasks")
        return send_emails(destinations, subject, body)
    except Exception as exc:
        # If an error occurs, retry the task
        raise self.retry(exc=exc)

