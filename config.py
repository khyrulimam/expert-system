import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", 'mysql://root:password@localhost/tht_expert')
SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 2

APP_NAME = 'ExpART'

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="

SESSION_USER_ID = "USERNAME"
