import pytest

from horus.users.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUserModel:
    def test_create_existance(self, user):
        user.name = "Mariam Elhadad"
        user.save()
        test_user = User.objects.get(name="Mariam Elhadad")
        assert user.name == test_user.name
        assert test_user.name == "Mariam Elhadad"

    def test_user_existance(self, user):
        assert User.objects.filter(username="username").exists() is True

    def test_email_is_unique(self, user):
        assert user._meta.get_field("email").unique is True

    def test_email_max_length(self, user):
        assert user._meta.get_field("email").max_length == 255

    def test_username_is_unique(self, user):
        assert user._meta.get_field("username").unique is True

    def test_username_max_length(self, user):
        assert user._meta.get_field("username").max_length == 100

    def test_name_max_length(self, user):
        assert user._meta.get_field("name").max_length == 255

    def test_is_superuser_for_user_is_false(self, user):
        assert user.is_superuser is False

    def test_superuser_is_superuser(self, superuser):
        assert superuser.is_superuser is True

    def test_superuser_is_staff(self, superuser):
        assert superuser.is_staff is True
