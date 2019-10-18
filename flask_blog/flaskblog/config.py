import os
import pymysql
pymysql.install_as_MySQLdb()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    MAIL_SERVER = 'smtp.qiye.aliyun.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ruj@hyee.com.cn'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
