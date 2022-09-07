import pytest


@pytest.mark.django_db
def test_ads_create(client, user, category, user_token):
    response = client.post(
        "/ad/create/",
        {
            "name": "new test ad",
            "price": 10,
            "description": "test description",
            "is_published": False,
            "author": user.id,
            "category": category.id
        },
        content_type="application/json",
        HTTP_AUTHORIZATION = f"Bearer {user_token}")

    assert response.status_code == 201
    assert response.data == {
        'Id': 2,
        'author': user.id,
        'category': category.id,
        'description': 'test description',
        'image': None,
        'is_published': False,
        'name': 'new test ad',
        'price': 10,
    }
