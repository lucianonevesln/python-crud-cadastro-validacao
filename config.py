import os


DB = os.environ.get('MYSQL_DATABASE_DB')
USER = os.environ.get('MYSQL_DATABASE_USER')
PASS = os.environ.get('MYSQL_DATABASE_PASSWORD')
DB_URL = os.environ.get('MYSQL_DATABASE_HOST')