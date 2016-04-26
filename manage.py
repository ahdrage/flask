from app import create_app, db
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager


app = create_app('default') # Note: pass an argument so we can have a few different configurations, for now we'll use default, and come back later
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
