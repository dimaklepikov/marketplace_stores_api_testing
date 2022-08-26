import pytest

from api import Item, User, Store
from mock_data import MockData
from constants import Headers
from schemas import UserSchema, StoreSchema, ItemSchema



#TODO: 
# 5) Add Allure report
# 6) Add Gitlab CI auto run tests


data = MockData()
@pytest.mark.critical_path
class TestCriticalPath:
    

    def test_registration(self, base_url):
        response = User(url=base_url).register(
            body=data.register_body,
            schema=UserSchema.registration,
            )
        
        assert response.status_code == 201
        assert response.response.get("message") == "User created successfully."
        assert response.response.get("uuid")
        
        
    def test_existing_register(self, base_url):
        response = User(url=base_url).register(
            body=data.register_body,
            schema=UserSchema.registration,
            )

        assert response.status_code == 400
        assert response.response.get("message") == "A user with that username already exists"
        assert response.response.get("uuid")


    def test_authentification(self, base_url):
        response = User(url=base_url).authentificate(
            body=data.register_body,
            schema=UserSchema.authentication
            )
        
        data.token = response.response.get("access_token")

        assert response.status_code == 200
        assert data.token
        

    def test_store_creation(self, base_url):
        response = Store(url=base_url).create(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.create_and_get
            )

        assert response.status_code == 201        
        assert response.response.get("name") == str(data.store_number)
        assert response.response.get("uuid")

      
    def test_getting_store(self, base_url):
        response = Store(url=base_url).get(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.create_and_get
            )

        assert response.status_code == 200       
        assert response.response.get("name") == str(data.store_number)
        data.store_id = response.response.get("uuid")
        assert data.store_id


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
    
    def test_delete_store_item(self, base_url):
        response = Item(url=base_url).delete(
            name=data.item_name,
            headers=Headers.auth(data.token),
            schema=ItemSchema.delete,
        )
        
        assert response.status_code == 200
        assert response.response.get("message") == "Item deleted."
        
    
    
    def test_get_deleted_store_item(self, base_url):
        response = Item(url=base_url).get(
            name=data.item_name,
            headers=Headers.auth(data.token),
            schema=ItemSchema.delete,
        )
        
        assert response.status_code == 404
        assert response.response.get("message") == "Item not found"    
    
    
    def test_delete_store(self, base_url):
        response = Store(url=base_url).delete(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.message
            )

        assert response.status_code == 200        
        assert response.response.get("message") == "Store deleted"
    
    
    def test_get_deleted_store(self, base_url):
        response = Store(url=base_url).get(
            name=data.store_number, 
            headers=Headers.auth(data.token),
            schema=StoreSchema.message
            )

        assert response.status_code == 404       
        assert response.response.get("message") == "Store not found"
