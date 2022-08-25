from jsonschema import validate
import logging

from custom_requests import Client
from models import ResponseModel


logger = logging.getLogger("api")
class User():
    def __init__(self, url):
        self.url = url
        self.client = Client()

    def register(self, body, schema):
        response = self.client.custom_request("POST", f'{self.url}/register', json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())

    def authentificate(self, body, schema):
        response = self.client.custom_request("POST", f'{self.url}/auth', json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())       
    
    def delete(self, user_id, headers, schema):
        response = self.client.custom_request("DELETE", f'{self.url}/user_info/{user_id}', headers=headers)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())

class Store():
    def __init__(self, url):
        self.url = url
        self.client = Client()

    def create(self, name, headers, schema):
        response =  self.client.custom_request("POST", f'{self.url}/store/{name}', headers=headers)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())        

    def get(self, name, headers, schema):
        response = self.client.custom_request("GET", f'{self.url}/store/{name}', headers=headers)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())    
class Item():
    def __init__(self, url):
        self.url = url
        self.client = Client()

    def create(self, name, headers, body, schema):
        response = self.client.custom_request("POST", f'{self.url}/item/{name}', headers=headers, json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())    
    
    def get(self, name, headers, schema):
        response = self.client.custom_request("GET", f'{self.url}/item/{name}', headers=headers)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        
        return ResponseModel(status=response.status_code, response=response.json())
