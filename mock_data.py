from faker import Faker
import random

fake = Faker()

class FakeData:
    
    
    def fake_register_body():
        return {
            'username': fake.user_name(),
            'password': fake.password()
        }


    def fake_store_number():
        return random.random()


    def fake_item_name():
        return fake.user_name()
    
    def fake_item_body(store_id):
        return {
        "price": fake.aba(),
        "store_id": store_id,
        "description": fake.catch_phrase(),
        "image": fake.file_path()
        }
    
