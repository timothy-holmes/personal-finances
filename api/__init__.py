from flask import Flask
from api.data import DataManager

application = Flask(__name__)

from api import endpoints

