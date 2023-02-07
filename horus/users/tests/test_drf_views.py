import pytest
from rest_framework.test import APIClient

from horus.users.models import User

pytestmark = pytest.mark.django_db
client = APIClient()


@pytest.mark.django_db
class TestUserRegister:
    def test_user_register_with_valid_data(self):
        user = {
            "name": "testing name",
            "email": "testing_123@gmail.com",
            "username": "testing123",
            "password": "Testing@123",
            "password_confirmation": "Testing@123",
        }
        responce = client.post("/users/register/", user)
        payload = responce.data
        assert responce.status_code == 201
        assert payload["message"] == "Registered Successfully"

    def test_user_without_username(self, request):
        user = {
            "name": "testing name",
            "email": "testing_123@gmail.com",
            "username": "",
            "password": "Testing@123",
            "password_confirmation": "Testing@123",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_without_name(self, request):
        user = {
            "name": "",
            "email": "testing_123@gmail.com",
            "username": "testing123",
            "password": "Testing@123",
            "password_confirmation": "Testing@123",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_without_email(self, request):
        user = {
            "name": "testing name",
            "email": "",
            "username": "testing123",
            "password": "Testing@123",
            "password_confirmation": "Testing@123",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_without_password(self, request):
        user = {
            "name": "testing name",
            "email": "testing_123@gmail.com",
            "username": "testing123",
            "password": "",
            "password_confirmation": "Testing@@123",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_without_password_confirmation(self, request):
        user = {
            "name": "testing name",
            "email": "testing_123@gmail.com",
            "username": "testing123",
            "password": "Testing@123",
            "password_confirmation": "",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_with_weak_password(self, request):
        user = {
            "name": "testing name",
            "email": "testing_123@gmail.com",
            "username": "testing123",
            "password": "Testing@@",
            "password_confirmation": "Testing@@",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_password_and_confirmation_not_identical(self, request):
        user = {
            "name": "testing name",
            "email": "testing_123@gmail.com",
            "username": "testing123",
            "password": "Testing@123",
            "password_confirmation": "Testing@12",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_with_email_already_exist(self, request):
        user = {
            "name": "testing name",
            "email": "horus1@gmail.com",
            "username": "testing123",
            "password": "Testing@123",
            "password_confirmation": "Testing@12",
        }
        User.objects.create(
            name="test test",
            username="horus123",
            email="horus1@gmail.com",
            password="horus_CSED2023",
        )
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_with_username_already_exist(self, request):
        user = {
            "name": "testing name",
            "email": "horus5@gmail.com",
            "username": "horus123",
            "password": "Testing@123",
            "password_confirmation": "Testing@12",
        }
        User.objects.create(
            name="test test",
            username="horus123",
            email="horus12@gmail.com",
            password="horus_CSED2023",
        )
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400

    def test_user_with_invalid_email(self, request):
        user = {
            "name": "testing name",
            "email": "horus5.v",
            "username": "horus1234",
            "password": "Testing@123",
            "password_confirmation": "Testing@12",
        }
        responce = client.post("/users/register/", user)
        assert responce.status_code == 400
