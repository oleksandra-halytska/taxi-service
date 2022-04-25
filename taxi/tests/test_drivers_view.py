from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from taxi.models import Driver

DRIVER_LIST_URL = reverse("taxi:driver-list")
SUCCESS_STATUS = 200


class PublicDriverTests(TestCase):
    def test_login_required_list(self):
        response = self.client.get(DRIVER_LIST_URL)

        self.assertNotEqual(response.status_code, SUCCESS_STATUS)

    def test_login_required_detail(self):
        driver = get_user_model().objects.create_user(
            username="someone",
            password="passsword",
            license_number="AAAA6555"
        )
        response = self.client.get(
            driver.get_absolute_url()
        )

        self.assertNotEqual(response.status_code, SUCCESS_STATUS)


class PrivateDriverTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="username",
            password="password"
        )
        self.client.force_login(self.user)

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(
            username="someone",
            password="passsword",
            license_number="AAAA6666"
        )

    def test_retrieve_drivers(self):
        response = self.client.get(DRIVER_LIST_URL)
        drivers = Driver.objects.all()

        self.assertEqual(response.status_code, SUCCESS_STATUS)
        self.assertEqual(
            list(response.context["driver_list"]),
            list(drivers)
        )
        self.assertTemplateUsed(response, "taxi/driver_list.html")

    def test_retrieve_detail_driver_information(self):
        driver = get_user_model().objects.create(
            username="name1",
            password="123456789",
            license_number="AAAA2222"
        )
        response = self.client.get(
            driver.get_absolute_url()
        )
        self.assertEqual(response.status_code, SUCCESS_STATUS)
        self.assertEqual(
            response.context["driver"],
            driver
        )
        self.assertTemplateUsed(response, "taxi/driver_detail.html")

    def test_create_driver(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345test",
            "password2": "user12345test",
            "first_name": "test_first",
            "last_name": "test_last",
            "license_number": "AAA11111",
        }
        self.client.post(reverse("taxi:driver-create"), data=form_data)

        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.license_number, form_data["license_number"])
