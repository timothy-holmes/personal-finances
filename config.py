import os

# get secret key from private folder
class Config():
    def __init__(self):
        self['secret_key'] = 'some_key'