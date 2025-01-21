import pytest
from pytest_bdd import scenario


@pytest.mark.django_db
@scenario('../test_02_access_control_logged_in_user/logged_in_user_access_verification.feature', 'Log in to Taxi Service web site and verify that logging process was successful')
def test_logged_in_access_control(setup_browser):
    pass
