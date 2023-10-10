import os

class Config(object):
    # May want to replace SECRET_KEY value with following command:
    # $ python -c 'import secrets; print(secrets.token_hex())'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
