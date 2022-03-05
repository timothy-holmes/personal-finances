import pandas as pd
from config import Config
from api.extract_transform import RequestHandler

class DataManager():
    config = Config()

    def __init__(self):
        # Load data from local file or pull from API then read from API
        requestor = None

        # list of data tables
        for x in ['_acc','_trans','_cat','_tag','_webh']:
            # path of table csv file if it exists
            persistent_data = self.config['PERSISTENT_DATA' + x.upper()]
            if persistent_data:
                # read csv file
                self.__dict__['df' + x] = pd.read_csv(persistent_data)
            else:
                try:
                    # new RequestHandler
                    if not requestor: requestor = RequestHandler()

                    # pass to another function to deal with 
                    self.pull_all()
                    self.__dict__['df' + x] = pd.write_csv('PERSISTENT_DATA_ACC')
                except:
                    print('Error loading data')

    def pull(self,map_field,requestor): # --> pandas.DataFrame
        # return summarised data as JSON
        map = api_map
        requestor