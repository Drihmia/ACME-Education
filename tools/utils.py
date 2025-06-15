#!/usr/bin/python3
'''
This script contains several utility functions
'''

from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_datetime():
    """
    Get the current date and time in Morocco timezone.
    It will adapt to the daylight saving time automatically.
    """

    # Get the current date and time in Morocco timezone using the built-in ZoneInfo class
    morocco_tz = ZoneInfo("Africa/Casablanca")

    # Get the current date and time in Morocco timezone
    current_datetime = datetime.now(morocco_tz).strftime("%Y %h %d at %H:%M:%S")
    return current_datetime


def is_true(value: str, option1: str, option2: str, option3: str):
    """ evaluate the value
    return:
     - option1 is value is true.
     - option2 if value is false.
     - option3 if value is something else, not boolen.
    """

    if isinstance(value, bool):
        if value == True:
            return option1
        elif value == False:
            return option2
    elif isinstance(value, int) and value.isdigit():
        if int(value) == 1:
            return option1
        elif int(value) == 0:
            return option2
    elif isinstance(value, str):
        if value.lower() == 'true':
            return option1
        elif value.lower() == 'false':
            return option2
    return option3


def log_file(message: str, file_path: str = 'logins.txt'):
    """ Log a message to a file

    Arguments:
    file_path: str: The path of the file to log the message to
    message: str: The message to log
    """

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{get_current_datetime()} - {message}\n")
