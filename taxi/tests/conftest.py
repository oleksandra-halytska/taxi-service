import os
import pytest

from playwright.sync_api import Playwright, Page
from django.contrib.auth import get_user_model
from taxi.models import Manufacturer, Trip
from taxi.tests.constants.constants import Constants
from taxi.tests.page_objects import (
    LoginPage,
    CarsPage,
    ManufacturersPage,
    DriversPage
)


pytest_plugins = [
    "taxi.tests.steps.steps"
]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


@pytest.fixture
def setup_browser(live_server, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(live_server.url)
    try:
        yield page
    finally:
        context.close()
        browser.close()


@pytest.mark.django_db
@pytest.fixture
def create_superuser() -> None:
    User = get_user_model()

    if not User.objects.filter(username="test").exists():
        User.objects.create_superuser(
            username="test",
            email="test@gmail.com",
            password="123456"
    )


@pytest.mark.django_db
@pytest.fixture
def create_manufacturer() -> None:
    Manufacturer.objects.create(
        name="test_manufacturer",
        country="country"
    )


@pytest.mark.django_db
@pytest.fixture
def create_trip() -> None:
    Trip.objects.create(
        name="test_manufacturer",
        country="country"
    )


@pytest.fixture
def login_page(setup_browser, create_superuser) -> object:
    return LoginPage(setup_browser)


@pytest.fixture
def cars_page(setup_browser) -> object:
    return CarsPage(setup_browser)


@pytest.fixture
def drivers_page(setup_browser) -> object:
    return DriversPage(setup_browser)


@pytest.fixture
def manufacturers_page(setup_browser) -> object:
    return ManufacturersPage(setup_browser)


@pytest.fixture
def make_page_fixture(
        login_page, cars_page, drivers_page, manufacturers_page
) -> object:
    def make(page_name):
        if page_name == Constants.LOGIN_PAGE:
            return login_page
        elif page_name == Constants.CARS_PAGE:
            return cars_page
        elif page_name == Constants.DRIVERS_PAGE:
            return drivers_page
        elif page_name == Constants.MANUFACTURERS_PAGE:
            return manufacturers_page
        else:
            raise ValueError(f"Unknown page: {page_name}")
    return make
