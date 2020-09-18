# Class of an endpoint
from enum import Enum
import requests

class Endpoint:

    def __init__(self, host, endpoint):
        self.host = host
        self.endpoint = endpoint
        self.tested = False
        self.uri = self.buildUri(host, endpoint)
    

    def buildUri(self, host, endpoint):
        '''
        - str host
        - str endpoint
        - r: str host/endpoint (cat'd)
        '''
        uri = "http://" + host + endpoint
        return uri

    
    def ping(self):

        response = requests.get(self.uri)

        # try to gen up a non-200: has auth!
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # was not a 200
            self.tested = True
            self.passed = True
            self.status = status
            self.grabbedheader = 'None Grabbed'
            return
        
        # was a 200: failed auth tet
        failedResp = response.headers
        status = response.status_code
        self.status = status
        self.grabbedheader = failedResp
        self.tested= True
        self.passed = False

        return 
        
    def __str__(self):
        return "Host: " + self.host + "\n" + "Suffix: " + self.endpoint + "\n" + "Tested: " + str(self.tested) + "\nLast Result: " + str(self.passed)

