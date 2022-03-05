from api import application
from api.extract_transform import RequestHandler

print('name from endpoints.py',__name__)

@application.route('/')
@application.route('/index')
def index():
    return "Hello, World!"