import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False