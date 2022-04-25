from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from random import choice

from taxi.models import Car, Manufacturer

CARS_LIST_URL = reverse("taxi:car-list")
CAR_NUM = 7
SUCCESS_STATUS = 200
PAGINATION_NUMBER = 3


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

        self.assertEqual(Manufacturer.objects.count(), objects_num - 1)
