import pytest

from playwright.sync_api import Playwright, Page
from .constants.constants import Constants
from .page_objects import LoginPage, CarsPage, ManufacturersPage, DriversPage


pytest_plugins = [
   "taxi.tests.steps.steps"
]


@pytest.fixture(scope="module")
def setup_browser(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    print("Launching browser page...")
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8000/")
    try:
        yield page
    finally:
        context.close()
        browser.close()
        print("Closing browser page...")


@pytest.fixture(scope="module")
def login_page(setup_browser):
    return LoginPage(setup_browser)


@pytest.fixture(scope="module")
def cars_page(setup_browser):
    return CarsPage(setup_browser)


@pytest.fixture(scope="module")
def drivers_page(setup_browser):
    return DriversPage(setup_browser)


@pytest.fixture(scope="module")
def manufacturers_page(setup_browser):
    return ManufacturersPage(setup_browser)


@pytest.fixture(scope="module")
def make_page_fixture(
        login_page, cars_page, drivers_page, manufacturers_page
):
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
