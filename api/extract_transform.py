import requests as rq
from config import Config # contains secret key

class RequestHandler():
# look up paramters for curl (-H, -d)
    def __init__(self):
        self.config = Config()
        self.api_map 
        token = self.config['SECRET_TOKEN']
        self.token_header = 'Authorization: Bearer ' + token
        assert self.get_specific_data('token_ping')

    def verify_token_validity(self,path,header): # --> bool
        #verify token validity
        check_token_response = self.get(self.config['BASE_PATH'] + '/util/ping',self.header)
        good_token = self.handle_response_status(check_token_response)
        return good_token

    def get(self,path,headers,params,data): # --> requests.Reponse
        if headers != None: headers = []
        headers = headers + self.token_header
        response = rq.get(path,headers,params,data)
        return response

    def get_data(self,path,headers,params,data): # --> list/dict (JSON) 
        path = ''
        for x in range(10): #
            response = self.get(self, path=path, headers=headers, params=params, data=data)
            # handle bad response/request
            good_request = self.handle_response_status(response)
            if good_request:
                response_data = response.json()
                next_path = response_data.get('links',{}).get('next',{})
                response_data[data].append(next_data)
            else:
                response_data = None
        return response_data[data]

    def handle_response_status(response): # --> int
        # unfinished
        def is_good():
            return True
        def lol(status):
            print('lol',status)
            return False
        def print_status(status):
            print(status)
            return False

        response_handlers = {
            200: is_good,
            400: print_status,
            401: print_status,
            404: print_status,
            418: lol
        }
        return response_handlers[response.status](response.status)

if __name__ == '__main__':
    # testing
    r = RequestHandler()
    test_request_good = r.get_data('http://timothyholmes.com.au/index.html',None)
    assert test_request_good[0] == 200
    test_request_bad = r.get_data('http://timothyholmes.com.au/thisdoesntexist',None)
    assert test_request_bad[0] != 200