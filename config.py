import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.getenv('SECRET_KEY', 'df6sdf768s7d68sd6f76sd8f76a9sd87f6a6f')
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite'))

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'db.sqlite'))

	
config = {
	'default': DevelopmentConfig,
	'development': DevelopmentConfig,
	'production': ProductionConfig
}
    
