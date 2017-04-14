import json
import requests


class Ufrn(object):

    def __init__(self, client_id, client_secret,
                 grant_type='client_credentials'):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__grant_type = grant_type
        _URL = 'http://apitestes.info.ufrn.br/authz-server/oauth/token?' + \
               'client_id={}&client_secret={}&grant_type={}'
        self.__access_token = requests.post(_URL.format(self.client_id(),
                                            self.client_secret(),
                                            self.grant_type())
                                            ).json().get('access_token')

    def client_id(self):
        '''Returns client_id'''
        return self.__client_id

    def client_secret(self):
        '''Returns client_secret'''
        return self.__client_secret

    def grant_type(self):
        '''Returns grant_type'''
        return self.__grant_type

    def access_token(self):
        '''Returns access_token'''
        return self.__access_token
