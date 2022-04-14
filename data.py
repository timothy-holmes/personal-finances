import pandas as pd
from api.config import Config
from api.request_handler import RequestHandler

class DataManager():
    config = Config()
    requestor = None
    dfs = {}

    def __init__(self):
        # list of data tables
        x = 'trans'
        if x:#for x in self.config.d['API_MAP'].keys():
            # path of table csv file if it exists
            persistent_data = None #self.config['PERSISTENT_DATA' + '_' + x.upper()]
            if persistent_data:
                pass
                # read csv file
                # self.dfs['df' + x] = pd.read_csv(persistent_data)
            else:
                #try:
                # new RequestHandler
                self.dfs['df_' + x] = self.pull_data(x)
                #pd.to_csv(self.config.d['CSV_PATH'])
                #except:
                #print('Error loading data')

    def pull_data(self,map_field): # --> pandas.DataFrame
        if not self.requestor: self.requestor = RequestHandler()
        # return summarised data as JSON
        map = self.config.d['API_MAP'][map_field]
        path = map['path']
        headers = None
        params = None
        # request
        data = self.requestor.get_data(path,headers)
        df = pd.json_normalize(data)
        data_flat = df.to_json()
        print(map_field,list(df.columns))
        return df

if __name__ == '__main__':
    data = DataManager()
    with open('C:/GitHub/trans.secret','w') as f:
        data.dfs['df_trans'].to_csv()
