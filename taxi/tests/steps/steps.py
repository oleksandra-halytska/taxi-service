from pytest_bdd import when, then, parsers
from ..page_objects.locators.locators import Locators


@when(parsers.parse("open '{page_name}' page"))
def open_page(page_name, make_page_fixture):
    page_object = make_page_fixture(page_name)
    page_object.click_on_link()


@when('the user enters valid credentials')
def enter_credentials(login_page):
    login_page.fill_username_field()
    login_page.fill_password_field()


@when('the user submits the form')
def submit_form(login_page):
    login_page.click_on_button()


@then('the user should be redirected to the home page')
def verify_home_page(setup_browser):
    assert setup_browser.url == setup_browser.url


@then(parsers.parse("'{text}' {role} is available on '{page_name}' page"))
def is_text_available(
        text: str, role: str, page_name: str, make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)

    assert page_object.is_element_exist(text, role), \
        (f"'{text}' text with {role} role is not available"
         f" on the {page_name} page.")


@when(parsers.parse("click on '{link_name}' link on '{page_name}' page"))
def click_on_the_button(
        link_name: str, page_name: str, make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)
    page_object.click_on_link_with_name(link_name)


@when(parsers.parse("click on '{button_name}' button on '{page_name}' page"))
def click_on_the_button(
        button_name: str, page_name: str, make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)
    page_object.click_on_button_with_name(button_name)


@when(parsers.parse(
    "fill the '{field_name}' field with '{text}' text on '{page_name}' page"
))
def fill_the_field_with_text(
        field_name: str, text: str, page_name: str, make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)
    page_object.fill_the_field_with_text(field_name, text)


@when(parsers.parse("Update object: '{object_attribs}' on '{page_name}'"
                    " page with '{updated_attribs}'"))
def perform_operation_on_page(
        page_name: str,
        object_attribs: str,
        updated_attribs: str,
        make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)
    page_object.click_on_object_update_button(object_attribs)
    page_object.update_object_with_values(updated_attribs)


@when(parsers.parse("Delete object: '{object_attribs}' on '{page_name}' page"))
def perform_operation_on_page(
        page_name: str,
        object_attribs: str,
        make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)
    page_object.click_on_object_delete_button(object_attribs)
