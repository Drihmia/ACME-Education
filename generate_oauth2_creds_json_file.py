#!/usr/bin/python3
"""This file helps to verify OAuth2 information."""
import os
from yagmail.oauth2 import get_oauth2_info


oauth2_creds_path = '~/oauth2_creds.json'
EMAIL_SEND = os.environ.get('ACME_EMAIL')
if not EMAIL_SEND:
    print('EMAIL_SEND is empty')
    exit(0)

oauth2_info = get_oauth2_info(oauth2_creds_path, EMAIL_SEND)

# IMPORTANT NOTE: I VE ALREADY SET THAT FOR OUR EMAIL.
