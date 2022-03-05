import requests as rq
from api.config import Config # contains secret key

class RequestHandler():
    def __init__(self):
        self.config = Config()
        token = self.config.d['SECRET_TOKEN']
        self.token_header = {'Authorization': 'Bearer {token}'.format(token=token)}
        assert self.verify_token_validity()

    def verify_token_validity(self): # --> bool
        #verify token validity
        check_token_response = self.get('/util/ping',None)
        good_token = self.handle_response_status(check_token_response)
        return good_token

    def get(self,path,headers): # --> requests.Reponse
        # if headers == None: headers = {}
        path = self.config.d['BASE_PATH'] + path
        # headers.update(self.token_header)
        # response = rq.get(path,headers)
        # return response

        payload=None
        headers = self.token_header

        response = rq.get(path,headers=headers,
        )
        print(response.text)
        return response

    def get_data(self,path,headers): # --> list/dict (JSON) 
        next_path = ''
        datas = []
        max_requests = self.config.d['MAX_REQUESTS']
        for x in range(max_requests): #
            response = self.get(path=path, headers=headers)
            good_request = self.handle_response_status(response)
            if good_request:
                data = response.json().get('data',{})
                next_path = data.get('links',{}).get('next',{})
                if type(data) == list:
                    datas += data
            if len(next_path) == 0: break
        return datas

    @staticmethod
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
        return response_handlers[response.status_code](response.status_code)

if __name__ == '__main__':
    # testing
    r = RequestHandler()
    test_request_good = r.get_data('http://timothyholmes.com.au/index.html',None)
    assert test_request_good[0] == 200
    test_request_bad = r.get_data('http://timothyholmes.com.au/thisdoesntexist',None)
    assert test_request_bad[0] != 200