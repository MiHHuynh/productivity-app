import os

class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = 'postgres://localhost/productivity-db'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True