from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from taxi.models import Manufacturer


class ManufacturerSearchTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_driver",
            password="password123"
        )
        self.client.login(username="test_driver", password="password123")

        self.manufacturer1 = Manufacturer.objects.create(
            name="Toyota", country="Japan")
        self.manufacturer2 = Manufacturer.objects.create(
            name="Ford", country="USA")

    def test_search_works_correctly(self):
        url = reverse("taxi:manufacturer-list")
        response = self.client.get(url, {"name": "Toy"})

        self.assertEqual(response.status_code, 200)

        results = response.context["manufacturer_list"]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Toyota")
