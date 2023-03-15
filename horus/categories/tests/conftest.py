import pytest
from rest_framework.test import APIClient

from horus.users.models import User


@pytest.fixture()
def user(db) -> User:
    return User.objects.create_user(
        name="Test user",
        username="username12345",
        email="test@gmail.com",
        password="Testing__123456",
    )


@pytest.fixture()
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.fixture
def client():
    client = APIClient()
    return client
