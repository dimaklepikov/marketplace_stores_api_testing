import requests

class User():
    def __init__(self, url):
        self.url = url

    def register_user(self, body):
        return requests.post(f'{self.url}/register', json=body) 

    def authentificate_user(self, body):
        return requests.post(f'{self.url}/auth', json=body)
    
    def delete_user(self, user_id, auth_key):
        return requests.delete(f'{self.url}/user_info/{user_id}', headers=auth_key)


class Store():
    def __init__(self, url):
         self.url = url

    def create_store(self, name, auth_key):
        return requests.post(f'{self.url}/store/{name}', headers={'Authorization': f'JWT {auth_key}'})

    def get_store(self, name, auth_key):
        return requests.get(f'{self.url}/store/{name}', headers={'Authorization': f'JWT {auth_key}'})
