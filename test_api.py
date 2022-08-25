import pytest

from api import Item, User, Store
from mock_data import FakeData
from constants import Headers
from schemas import UserSchema, StoreSchema, ItemSchema



#TODO: 
# 1)Add critical path test group 
# 3) Refactor code at MockData class
# 5) Add Allure report
# 6) Add Gitlab CI auto run tests
class MockData(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MockData, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.register_body = FakeData.fake_register_body()
        self.store_number = FakeData.fake_store_number()
        self.token = None
        self.store_id = None
        self.item_id = None
        self.item_name = FakeData.fake_item_name()
        self.item_body = FakeData.fake_item_body(self.store_id)

data = MockData()

class TestApi:

    @pytest.mark.api1
    def test_registration(self, base_url):
        response = User(url=base_url).register(
            body=data.register_body,
            schema=UserSchema.registration,
            )
        
        assert response.status_code == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')

    @pytest.mark.api1
    def test_existing_register(self, base_url):
        response = User(url=base_url).register(
            body=data.register_body,
            schema=UserSchema.registration,
            )

        assert response.status_code == 400
        assert response.response.get('message') == 'A user with that username already exists'
        assert response.response.get('uuid')


    @pytest.mark.api1
    def test_authentification(self, base_url):
        response = User(url=base_url).authentificate(
            body=data.register_body,
            schema=UserSchema.authentication
            )
        
        data.token = response.response.get('access_token')

        assert response.status_code == 200
        assert data.token
        

    @pytest.mark.api1
    def test_store_creation(self, base_url):
        response = Store(url=base_url).create(
            name=data.store_number, 
            headers=Headers.auth_header(data.token),
            schema=StoreSchema.create_and_get
            )

        assert response.status_code == 201        
        assert response.response.get('name') == str(data.store_number)
        assert response.response.get('uuid')


    @pytest.mark.api1
    def test_getting_store(self, base_url):
        response = Store(url=base_url).get(
            name=data.store_number, 
            headers=Headers.auth_header(data.token),
            schema=StoreSchema.create_and_get
            )

        assert response.status_code == 200       
        assert response.response.get('name') == str(data.store_number)
        data.store_id = response.response.get('uuid')
        assert data.store_id
    

    @pytest.mark.api1
    def test_existing_store_creation(self, base_url):
        response = Store(url=base_url).create(
            name=data.store_number, 
            headers=Headers.auth_header(data.token),
            schema=StoreSchema.existing_store_cretion
            )

        assert response.status_code == 400
        assert response.response.get('message') == f'''A store with name '{data.store_number}' already exists.'''
    
    @pytest.mark.api1
    def test_create_store_item(self, base_url):
        response = Item(url=base_url).create(
            name=data.item_name,
            headers=Headers.auth_header(data.token),
            body=data.item_body,
            schema=ItemSchema.create_and_get,
            )
        data.item_id = response.response.get('itemID')
        
        assert response.status_code == 201
        assert response.response.get('name') == data.item_name
        assert response.response.get('image') == data.item_body.get('image') 
        
    @pytest.mark.api1
    def test_get_store_item(self, base_url):
        response = Item(url=base_url).get(
            name=data.item_name,
            headers=Headers.auth_header(data.token),
            schema=ItemSchema.create_and_get,
        )
        
        assert response.status_code == 200
        assert response.response.get('name') == data.item_name
        assert response.response.get('price') == float(f'{data.item_body.get("price")}.0')
        assert response.response.get('item_ID') != data.item_id
