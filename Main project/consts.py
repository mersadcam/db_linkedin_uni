DB_NAME = "LinkedInDB"


def debug(**kwargs):
    for key in kwargs:
        print(f'{key}: {kwargs[key]}')


class Messages:
    ERR_INVALID_EMAIL_OR_PASSWORD = "Invalid email or password."
    DEFAULT_HEAD_LINE = "Hi! I'm using LinkedIn"
