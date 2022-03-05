from api import application
from data import DataManager

data_handler = DataManager()

@application.route('/')
@application.route('/index')
def index():
    return data_handler.dfs['df_acc'].to_html()