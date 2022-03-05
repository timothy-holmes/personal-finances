from flask import Flask
from data import DataManager

application = Flask(__name__)

from api import endpoints

