from app import create_app #TODO: Make a create_app function
from flask.ext.script import Manager

app = create_app('default') # Note: pass an argument so we can have a few different configurations, for now we'll use default, and come back later
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
