from pytest_bdd import when, then, parsers


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
    assert setup_browser.url == "http://localhost:8000/"


@then(parsers.parse("'{text}' {role} is available on '{page_name}' page"))
def is_text_available(
        text: str, role: str, page_name: str, make_page_fixture: callable
):
    page_object = make_page_fixture(page_name)

    assert page_object.is_element_exist(text, role), \
        f"'{text}' text with {role} role is not available on the {page_name} page."
