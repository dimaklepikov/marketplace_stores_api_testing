import pytest
import allure

from api import Item, User, Store
from mock_data import MockData
from constants import Headers
from schemas import UserSchema, StoreSchema, ItemSchema



#TODO: 
# Add Allure steps to each test case

data = MockData()
@pytest.mark.critical_path
class TestCriticalPath:
    
    @allure.feature("User")
    @allure.story("Register new user")
    def test_register_user(self, base_url):
        response = User(url=base_url).register(
            body=data.register_body,
            schema=UserSchema.registration,
            )
        with allure.step("Check response status code"):
            assert response.status_code == 201
        with allure.step("Check response message if user created"):
            assert response.response.get("message") == "User created successfully."
        with allure.step("Check if user id is avaliable"): 
            assert response.response.get("uuid")
        
    @allure.feature("User")
    @allure.story("Register existing user")        
    def test_register_existing_user(self, base_url):
        response = User(url=base_url).register(
            body=data.register_body,
            schema=UserSchema.registration,
            )
        with allure.step("Check response status code is bad request"):
            assert response.status_code == 400
        with allure.step("Check response message if user already exists"):
            assert response.response.get("message") == "A user with that username already exists"
        with allure.step("Check exising user id"):
            assert response.response.get("uuid")

    @allure.feature("User")
    def test_authentificate(self, base_url):
        response = User(url=base_url).authentificate(
            body=data.register_body,
            schema=UserSchema.authentication
            )
        
        data.token = response.response.get("access_token")

        assert response.status_code == 200
        assert data.token
        
    @allure.feature("Store")
    def test_create_store(self, base_url):
        response = Store(url=base_url).create(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.create_and_get
            )

        assert response.status_code == 201        
        assert response.response.get("name") == str(data.store_number)
        assert response.response.get("uuid")

    @allure.feature("Store")
    def test_get_store(self, base_url):
        response = Store(url=base_url).get(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.create_and_get
            )

        assert response.status_code == 200       
        assert response.response.get("name") == str(data.store_number)
        data.store_id = response.response.get("uuid")
        assert data.store_id

    @allure.feature("Store")
    def test_create_store_item(self, base_url):
        response = Item(url=base_url).create(
            name=data.item_name,
            headers=Headers.auth(data.token),
            body=data.item_body,
            schema=ItemSchema.create_and_get,
            )
        data.item_id = response.response.get("itemID")
        
        assert response.status_code == 201
        assert response.response.get("name") == data.item_name
        assert response.response.get("image") == data.item_body.get("image") 
    
    @allure.feature("Store item")
    def test_get_store_item(self, base_url):
        response = Item(url=base_url).get(
            name=data.item_name,
            headers=Headers.auth(data.token),
            schema=ItemSchema.create_and_get,
        )
        
        assert response.status_code == 200
        assert response.response.get("name") == data.item_name
        assert response.response.get("price") == float(f"{data.item_body.get('price')}.0")
        assert response.response.get("item_ID") != data.item_id

    @allure.feature("Store item")
    def test_create_existing_store_item(self, base_url):
        response = Item(url=base_url).create(
            name=data.item_name,
            headers=Headers.auth(data.token),
            body=data.item_body,
            schema=ItemSchema.delete,
            )
        data.item_id = response.response.get("itemID")
        
        assert response.status_code == 400
        assert response.response.get("message") == f"An item with name {data.item_name} already exists."   

    
    @allure.feature("Store item")
    def test_delete_store_item(self, base_url):
        response = Item(url=base_url).delete(
            name=data.item_name,
            headers=Headers.auth(data.token),
            schema=ItemSchema.delete,
        )
        
        assert response.status_code == 200
        assert response.response.get("message") == "Item deleted."
        
    
    @allure.feature("Store item")
    def test_get_deleted_store_item(self, base_url):
        response = Item(url=base_url).get(
            name=data.item_name,
            headers=Headers.auth(data.token),
            schema=ItemSchema.delete,
        )
        
        assert response.status_code == 404
        assert response.response.get("message") == "Item not found"    
    
    
    @allure.feature("Store item")
    def test_delete_store(self, base_url):
        response = Store(url=base_url).delete(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.message
            )

        assert response.status_code == 200        
        assert response.response.get("message") == "Store deleted"
    
    @allure.feature("Store item")
    def test_get_deleted_store(self, base_url):
        response = Store(url=base_url).get(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.message
            )

        assert response.status_code == 404       
        assert response.response.get("message") == "Store not found"
