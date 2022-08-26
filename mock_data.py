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
