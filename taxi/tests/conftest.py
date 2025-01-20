import os
import pytest

from playwright.sync_api import Playwright, Page
from django.contrib.auth import get_user_model
from taxi.tests.constants.constants import Constants
from taxi.tests.page_objects import LoginPage, CarsPage, ManufacturersPage, DriversPage


pytest_plugins = [
    "taxi.tests.steps.steps"
]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


# @pytest.fixture
# def admin_client(base_url, admin_credentials):
#     return AdminApiClient(base_url, **admin_credentials)
#
#
# @pytest.fixture
# def user(admin_client):
#     _user = User(name="Susan", username=f"testuser-{uuid4()}", password="P4$$word")
#     admin_client.create_user(_user)
#     yield _user
#     admin_client.delete_user(_user)

@pytest.fixture
def anyio_backend():

    return 'asyncio'


@pytest.fixture
def setup_browser(live_server, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
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
