from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer

MANUFACTURER_LIST_URL = reverse("taxi:manufacturer-list")
SUCCESS_STATUS = 200
MANUFACTURER_NUM = 4


class PublicManufacturerTests(TestCase):
    def test_login_required_list(self):
        response = self.client.get(MANUFACTURER_LIST_URL)

        self.assertNotEqual(response.status_code, SUCCESS_STATUS)


class PrivateManufacturerTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="username",
            password="password"
        )
        self.client.force_login(self.user)

    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(
            name="name1",
            country="country1"
        )
        Manufacturer.objects.create(
            name="name2",
            country="country2"
        )

    def test_retrieve_manufacturers(self):
        response = self.client.get(MANUFACTURER_LIST_URL)
        manufacturers = Manufacturer.objects.all()

        self.assertEqual(response.status_code, SUCCESS_STATUS)
        self.assertEqual(
            list(response.context["manufacturer_list"]),
            list(manufacturers)
        )
        self.assertTemplateUsed(response, "taxi/manufacturer_list.html")

    def test_delete_manufacturer(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )
        objects_num = Manufacturer.objects.count()

        self.client.delete(
            reverse(
                "taxi:manufacturer-delete",
                kwargs={"pk": manufacturer.id}
            )
        )

        self.assertEqual(Manufacturer.objects.count(), objects_num - 1)
