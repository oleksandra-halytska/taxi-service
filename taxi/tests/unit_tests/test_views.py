from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from random import choice

from taxi.models import Manufacturer, Driver, Car

MANUFACTURER_LIST_URL = reverse("taxi:manufacturer-list")
DRIVER_LIST_URL = reverse("taxi:driver-list")
SUCCESS_STATUS = 200
CARS_LIST_URL = reverse("taxi:car-list")
PAGINATION_NUMBER = 3
MANUFACTURER_NUM = 4
CAR_NUM = 7


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


class PublicCarTests(TestCase):
    def test_login_required_list(self):
        response = self.client.get(CARS_LIST_URL)

        self.assertNotEqual(response.status_code, SUCCESS_STATUS)

    def test_login_required_detail(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )
        car = Car.objects.create(
            model="model",
            manufacturer=manufacturer
        )
        response = self.client.get(
            car.get_absolute_url()
        )

        self.assertNotEqual(response.status_code, SUCCESS_STATUS)


class PrivateCarTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="username",
            password="password"
        )
        self.client.force_login(self.user)

    @classmethod
    def setUpTestData(cls):
        manufacturer1 = Manufacturer.objects.create(
            name="name1",
            country="Ukraine"
        )
        manufacturer2 = Manufacturer.objects.create(
            name="name2",
            country="country"
        )
        for car_num in range(CAR_NUM):
            Car.objects.create(
                model=f"model{car_num + 1}",
                manufacturer=choice(
                    (
                        manufacturer1,
                        manufacturer2
                    )
                )
            )

    def test_retrieve_cars(self):
        response = self.client.get(CARS_LIST_URL)
        cars = Car.objects.all()

        self.assertEqual(response.status_code, SUCCESS_STATUS)
        self.assertEqual(
            list(response.context["car_list"]),
            list(cars)[:PAGINATION_NUMBER]
        )
        self.assertTemplateUsed(response, "taxi/car_list.html")

    def test_retrieve_detail_car_information(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )
        car = Car.objects.create(
            model="to_check",
            manufacturer=manufacturer
        )
        response = self.client.get(
            car.get_absolute_url()
        )
        self.assertEqual(response.status_code, SUCCESS_STATUS)
        self.assertEqual(
            response.context["car"],
            car
        )
        self.assertTemplateUsed(response, "taxi/car_detail.html")

    def test_pagination_is_three(self):
        response = self.client.get(CARS_LIST_URL)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(len(response.context['car_list']) == PAGINATION_NUMBER)

    def test_delete_car(self):
        manufacturer = Manufacturer.objects.create(
            name="name",
            country="country"
        )
        car = Car.objects.create(
            model="model",
            manufacturer=manufacturer
        )
        objects_num = Car.objects.count()

        self.client.delete(
            reverse(
                "taxi:car-delete",
                kwargs={"pk": car.id}
            )
        )

        self.assertEqual(Car.objects.count(), objects_num - 1)
