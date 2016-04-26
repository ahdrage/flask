from Flask import Blueprint
main = Blueprint('main', __name__)
from . import views, forms #let's import the views and forms into here too
