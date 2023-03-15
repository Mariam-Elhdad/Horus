import pytest

from horus.categories.models import Category

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestCategoryViewSet:
    def test_list_categories(self, auth_client):
        request = auth_client.get("/categories/")
        assert request.status_code == 200
        Category.objects.create(name="Safary")
        category = Category.objects.get(name="Safary")
        request = auth_client.get("/categories/")
        assert request.status_code == 200
        assert request.data[0]["name"] == "Safary"
        assert request.data[0]["id"] == category.id

    def test_retrieve_specific_category(self, auth_client):
        Category.objects.create(name="Pharaonic")
        category = Category.objects.get(name="Pharaonic")
        request = auth_client.get(f"/categories/{category.name}/")
        assert request.status_code == 200

    def test_fail_unauth_user_to_retrieve(self, client):
        request = client.get("/categories/")
        assert request.status_code == 401
