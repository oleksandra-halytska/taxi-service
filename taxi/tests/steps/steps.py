import pytest

from pytest_bdd import when, then, scenarios
from taxi.tests.page_objects.login_page import LoginPage


@pytest.fixture
def login_page(setup_browser):
    return LoginPage(setup_browser)


@when("opens login page")
def open_login_page(login_page):
    login_page.click_on_login_link()


@when("the user enters valid credentials")
def enter_credentials(login_page):
    login_page.fill_username_field()
    login_page.fill_password_field()


@when("the user submits the form")
def submit_form(login_page):
    login_page.click_on_login_button()


@then("the user should be redirected to the home page")
def verify_home_page(setup_browser):
    assert setup_browser.url == "http://localhost:8000/"
