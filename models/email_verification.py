import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EmailVerifier:
    def __init__(self):
        self.api_key = os.getenv('EMAIL_VERIFICATION_API_KEY')
        if not self.api_key:
            raise ValueError('API key is not defined')

    def check_email_exists_zero_bounce(self, email: str) -> bool:
        """
        Checks if an email address exists using a third-party email verification service.

        :param email: The email address to verify.
        :return: A boolean indicating if the email exists.
        """
        url = 'https://api.zerobounce.net/v2/validate'
        params = {
            'email': email,
            'api_key': self.api_key,
            'ip_address': '',
        }

        response = requests.get(url, params=params)

        if response.ok:
            data = response.json()
            if data.get("status") == "valid":
                return True
            else:
                return False
            print("data:\n", data)
            return data.get('is_valid', False)  # Adjust based on the actual response
        else:
            raise Exception('Email verification service error')
    def check_email_exists_mail_gun(self, address: str) -> bool:
        """Validate an email address using Mailgun's API."""

        # Mailgun API URL for address validation
        url = f'https://api.mailgun.net/v3/address/validate'
        params = {"address": address}
        # Make the request
        response = requests.get(
            url,
            params=params,
            auth=('api', self.api_key)
        )

        # Check the response
        print("status_code:", response.status_code)
        if response.status_code == 200:
            data = response.json()
            print("data:", data)
            if "result" in data:
                if data.get("result") == "deliverable":
                    return True
                return False
            return False
            print('Validation successful:', )
        else:
            print('Failed to validate email:', response.status_code, response.text)
            return False


