DB_NAME = "LinkedInDB"


def debug(**kwargs):
    for key in kwargs:
        print(f'{key}: {kwargs[key]}')


class Columns:
    # Profile:
    FIRSTNAME = 'profile_first_name'
    LASTNAME = 'profile_last_name'
    HEADLINE = 'profile_headline'
    COUNTRY = 'profile_country'
    BIRTHDAY = 'profile_birthday'
    ADDR = 'profile_address'
    ABOUT = 'profile_about'

    # User:
    EMAIL = 'user_email'
    UUID = 'user_uuid'
    PASSWORD = 'user_password'
    TOKEN = 'user_token'

class Messages:
    ERR_INVALID_EMAIL_OR_PASSWORD = "Invalid email or password."
    DEFAULT_HEAD_LINE = "Hi! I'm using LinkedIn"
