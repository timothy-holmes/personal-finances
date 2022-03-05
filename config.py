class Config():
    def __init__(self):
        self.d = {}
        with open('../token.secret','r') as f:
            self.d['SECRET_TOKEN'] = f.read()
        self.d['BASE_PATH'] = 'https://api.up.com.au/api/v1'
        self.d['API_MAP'] = {
            '_acc': {'path': '/accounts'},
            '_trans': {'path': '/transactions'},
            '_cat': {'path': '/categories'},
            '_tag': {'path': '/tags'},
            '_webh': {'path': '/webhooks'}
        }
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