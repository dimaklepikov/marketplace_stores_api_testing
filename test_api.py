import pytest

from api import User, Store
from mock_data import fake_register_body, fake_store_number


class MockData(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MockData, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.body = fake_register_body()
        self.store_number = fake_store_number()
        self.token = None

data = MockData()

class TestApi:

    @pytest.mark.api
    def test_registration(self, base_url):
        response = User(url=base_url).register_user(body=data.body)

        assert response.status_code == 201
        assert response.json().get('message') == 'User created successfully.'
        assert response.json().get('uuid')


    @pytest.mark.api
    def test_existing_register(self, base_url):
        response = User(url=base_url).register_user(body=data.body)

        assert response.status_code == 400
        assert response.json().get('message') == 'A user with that username already exists'
        assert response.json().get('uuid')


    @pytest.mark.api
    def test_authentification(self, base_url):
        response = User(url=base_url).authentificate_user(body=data.body)
        data.token = response.json().get('access_token')

        assert response.status_code == 200
        assert data.token
        

    @pytest.mark.api
    def test_store_creation(self, base_url):
        response = Store(url=base_url).create_store(name=data.store_number, auth_key=data.token)

        assert response.status_code == 201        
        assert response.json().get('name') == str(data.store_number)
        assert response.json().get('uuid')


    @pytest.mark.api
    def test_getting_store(self, base_url):
        response = Store(url=base_url).get_store(name=data.store_number, auth_key=data.token)

        assert response.status_code == 200       
        assert response.json().get('name') == str(data.store_number)
        assert response.json().get('uuid')
    

    @pytest.mark.api
    def test_existing_store_creation(self, base_url):
        response = Store(url=base_url).create_store(name=data.store_number, auth_key=data.token)

        assert response.status_code == 400
        assert response.json().get('message') == f'''A store with name '{data.store_number}' already exists.'''
