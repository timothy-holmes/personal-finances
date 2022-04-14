from api import application
from data import DataManager
import random

data_handler = DataManager()

@application.route('/')
@application.route('/index')
def index(csv=False):
    return data_handler.dfs['df_trans'].to_html()