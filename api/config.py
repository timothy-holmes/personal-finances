class Config():
    def __init__(self):
        self.d = {'DEBUG': True}

        # token
        with open('C:/GitHub/personal-finances/api/token.secret','r') as f:
            self.d['SECRET_TOKEN'] = f.read()
        
        # api info
        self.d['BASE_PATH'] = 'https://api.up.com.au/api/v1'
        self.d['API_MAP'] = {
            'acc': {'path': '/accounts'},
            'trans': {'path': '/transactions'},
            'cat': {'path': '/categories'},
            'tag': {'path': '/tags'},
            'webh': {'path': '/webhooks'}
        }

        # app settings
        if self.d['DEBUG']:
            self.d['MAX_REQUESTS'] = 2
        else:
            self.d['MAX_REQUESTS'] = 100        
        self.d['CSV_PATH'] = 'data.csv.secret'

if __name__ == '__main__':
    import requests,json
    config = Config()
    path = config.d['BASE_PATH'] + '/transactions'
    headers = {
        'Authorization': ' '.join(['Bearer',config.d['SECRET_TOKEN']])
    }
    params = {
        'page[size]': 1
    }
    data = None
    response = requests.get(path,headers=headers,params=params)
    if response.status_code == 200:
        print(json.dumps(response.json(),indent=4))
    else:
        print(response.status_code)