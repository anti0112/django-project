from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, AdFactory

pytest_plugin = 'tests.fixtures'

register(UserFactory)
register(CategoryFactory)
register(AdFactory)