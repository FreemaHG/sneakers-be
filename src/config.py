import os

from dotenv import load_dotenv

load_dotenv()

PATH = os.path.dirname(os.path.realpath(__file__))

DEBUG = os.environ.get('DEBUG', False)

DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASSWORD')

ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS')

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')
