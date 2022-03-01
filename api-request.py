from requests import get
from config import Config # contains secret key

class RequestHandler():
# look up paramters for curl (-H, -d)

    def __init__(self):
        config = Config()
        token = config['secret_key']
        self.base_path = 'https://api.up.com.au/api/v1'
        self.header = 'Authorization: Bearer ' + token
        #verify token validity
        check_token = self.get(self.base_path + '/util/ping',self.header)
        if check_token == 200:
            print('Sucess')
        else:
            print('Error creating RequestHandler (response {status})'.format(status=check_token))

    def get(self,path,headers,params,data):
        if headers != None:
            header = self.header + headers
        response = requests.get(path,headers,params,data)
        return response

    def get_data(self,path,headers,params,data):
        path = ''
        response = self.get(self,path,headers,params,data)
        # handle bad response/request
        if response.status != 200:
            handled_error_message = self.handle_bad_response(response)
            print(handled_error_message)
            return None
        else:
            response_data = response.json()
            next_path = response_data['links']['next']
            if next_path:
                response_data[data].append(self.get_data(self,next_path,headers,params,data)) # recursion
        return response_data[data]

    def handle_bad_response(response):
        # unfinished
        bad_response_handlers = {
            400: 0,
            401: 0,
            404: 0,
            418: 'lol'
        }
        return bad_response_handlers[response.status](response.status)

class ApiMap(): # unfinished
    # learn how to map API?
    def get_endpoint(self,resource_str,data_source,data_dict):
        # do stuff based on required resource and given data
        return {
            'path': path, 
            'extra_header': extra_header, 
            'extra_params': extra_params
            }
    def get_endpoint(self,**kwargs):
        object_map = {
            'accounts': {'parent': 'user', 'children': 'special'}
        }
        def account_path():
            path = '/accounts'
            if kwargs['account_id']:
                return path + '/accounts/{id}'.format(id=kwargs['account_id']) 
        def transactions():
            path = '/transactions'
        endpoints = {
            'accounts': {'path': self.accounts_path(), 'func': 0},
            'transactions': {}
        }
        return endpoints


if __name__ == '__main__':
    # testing
    r = RequestHandler()
    test_request_good = r.get_data('http://timothyholmes.com.au/index.html',None)
    assert test_request_good[0] == 200
    test_request_bad = r.get_data('http://timothyholmes.com.au/thisdoesntexist',None)
    assert test_request_bad[0] != 200

    r = RequestHandler()
    r.token = 'demo'
    path = 