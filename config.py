import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Configs for Email notification for 500 errors
	MAIL_SERVER = os.getenv('MAIL_SERVER', 'default-mail-server')
	MAIL_PORT = os.getenv('MAIL_PORT', 25)
	MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.getenv('MAIL_USERNAME')
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
	ADMINS = ['sweetytweetypy@gmail.com']

	POSTS_PER_PAGE = 5
