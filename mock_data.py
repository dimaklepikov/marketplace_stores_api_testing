from faker import Faker
import random

fake = Faker()

def fake_register_body():
    return {
        'username': fake.user_name(),
        'password': fake.password()
    }

def fake_store_name():
    return random.random()