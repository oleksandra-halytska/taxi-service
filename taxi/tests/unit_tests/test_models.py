from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )

        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="username",
            password="password"
        )

        self.assertEqual(
            str(driver),
            f"{driver.username}"
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )
        car = Car.objects.create(
            model="model",
            manufacturer=manufacturer
        )
        self.assertEqual(
            str(car),
            f"{car.model}"
        )

    def test_create_driver_with_license_number(self):
        username = "username"
        password = "password"
        license_number = "AAAA1234"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )
        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)

    def test_car_get_absolute_url(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )
        car = Car.objects.create(
            model="model",
            manufacturer=manufacturer
        )
        self.assertEquals(car.get_absolute_url(), f'/cars/{car.id}/')

    def test_driver_get_absolute_url(self):
        driver = get_user_model().objects.create_user(
            username="name",
            password="0000000"
        )
        self.assertEquals(driver.get_absolute_url(), f'/drivers/{driver.id}/')
