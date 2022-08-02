import pytest



from api import User, Store
# from constants import BASE_URL
from mock_data import fake_register_body, fake_store_name

body = fake_register_body()
store_name = fake_store_name()

# Create HTML report
class TestApi:
    # @pytest.fixture(scope="session")
    # def url(pytestconfig):
    #     return pytestconfig.getoption("url")

    @pytest.mark.api
    def test_registration(self, base_url):
        response = User(url=base_url).register_user(body=body)
        assert response.status_code == 201
        assert response.json().get('message') == 'User created successfully.'
        assert response.json().get('uuid')


    @pytest.mark.api
    def test_existing_register(self, base_url):
        response = User(url=base_url).register_user(body=body)

        assert response.status_code == 400
        assert response.json().get('message') == 'A user with that username already exists'
        assert response.json().get('uuid')


    @pytest.mark.api
    def test_authentification(self, base_url):
        response = User(url=base_url).authentificate_user(body=body)

        assert response.status_code == 200
        assert response.json().get('access_token')
        global token 
        token = response.json().get('access_token')
        

    @pytest.mark.api
    def test_store_creation(self, base_url):
        response = Store(url=base_url).create_store(name=store_name, auth_key=token)

        assert response.status_code == 201        
        assert response.json().get('name') == str(store_name)
        assert response.json().get('uuid')


    @pytest.mark.api
    def test_getting_store(self, base_url):
        response = Store(url=base_url).get_store(name=store_name, auth_key=token)
        assert response.status_code == 200       
        assert response.json().get('name') == str(store_name)
        assert response.json().get('uuid')
    

    @pytest.mark.api
    def test_existing_store_creation(self, base_url):
        response = Store(url=base_url).create_store(name=store_name, auth_key=token)

        assert response.status_code == 201
        assert response.json().get('message') == f'''A store with name '{store_name}' already exists.'''
