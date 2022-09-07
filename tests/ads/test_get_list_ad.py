import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client, user):
    ads_factories = AdFactory.create_batch(10)

    response = client.get("/ad/?page=1")

    ads = []
    for ad in ads_factories:
        ads.append({
            "Id": ad.Id,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": "",
            "image": ad.image.url if ad.image else None,
        })

    expected_response = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": ads,
        
    }

    assert response.status_code == 200
    assert response.json() == expected_response
