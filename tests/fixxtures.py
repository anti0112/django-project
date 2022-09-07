import pytest

@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = "anti"
    password = "123qwe"
    role = "admin"
    
    django_user_model.object.create_user(username=username, password=password, role=role)
    response = client.post(
        "user/token/",
        {"username": username, "password": password},
        format='json'
        )
    return response.data['access']
    
    
    
