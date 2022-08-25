import requests

class User():
    def __init__(self, url):
        self.url = url

    def register(self, body):
        return requests.post(f'{self.url}/register', json=body) 

    def authentificate(self, body):
        return requests.post(f'{self.url}/auth', json=body)
    
    def delete(self, user_id, headers):
        return requests.delete(f'{self.url}/user_info/{user_id}', headers=headers)


class Store():
    def __init__(self, url):
         self.url = url

    def create(self, name, headers):
        return requests.post(f'{self.url}/store/{name}', headers=headers)

    def get(self, name, headers):
        return requests.get(f'{self.url}/store/{name}', headers=headers)
    
class Item():
    def __init__(self, url):
         self.url = url
         
    def create(self, name, headers, body):
        return requests.post(f'{self.url}/item/{name}', headers=headers, json=body)
    
    def get(self, name, headers):
        return requests.get(f'{self.url}/item/{name}', headers=headers)
