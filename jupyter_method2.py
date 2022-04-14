# Pull Up Bank data using API

#%%
# load tokens

with open('C:/GitHub/personal-finances/api/token.secret','r') as f:
    tokens = {v.split()[0]: v.split()[1] for v in f.read().splitlines()}

for name,t in tokens.items():
    print(name,t)

#%%

# check tokens
import requests

base_path = 'https://api.up.com.au/api/v1'

for name,t in tokens.items():
    token_header = {'Authorization': 'Bearer {token}'.format(token=t)}
    ping_response = requests.get(base_path + '/util/ping',headers=token_header)
    print(name,ping_response)

# %%

import random, json
import pandas as pd

def get_with_token(path,token):
    token_header = {'Authorization': 'Bearer {token}'.format(token=t)}
    if not base_path in path:
        path = base_path + path
    response = requests.get(path,headers=token_header)
    return response

def get_data(token,max_requests):
    path = '/transactions'
    data = []

    for x in range(max_requests):
        response = get_with_token(path,token)
        new_data = response.json().get('data',[])
        data += new_data
        next_path = response.json().get('links',{}).get('next',None)
        print(
            x,
            'path:',path[-36:-28],
            'status:',response.status_code,
            'data',len(new_data) > 0
        )
        if next_path == None:
            break
        else:
            path = next_path
            print(x,'next_path',next_path[-36:-28])  
    return data

tokens = {str(random.randint(a=1000000,b=9999999))+'.secret': token for name,token in tokens.items()}

for name,t in tokens.items():
    try:
        with open(name + '.csv','w') as f:
            token_header = {'Authorization': 'Bearer {token}'.format(token=t)}
            data = get_data(token=t,max_requests=100)
            df = pd.json_normalize(data)
            data_flat = df.to_csv()
            df.to_excel(name + '.xlsx')
            f.write(json.dumps(data_flat,indent=4))
            print('datafile',name)
    except Exception as e:
        print('error',e)
# %%
