from flask import Flask

application = Flask(__name__)

from api import endpoints

