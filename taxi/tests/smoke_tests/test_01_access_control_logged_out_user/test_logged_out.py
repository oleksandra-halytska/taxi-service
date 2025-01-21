import pytest
from pytest_bdd import scenario


@pytest.mark.django_db
@scenario('../test_01_access_control_logged_out_user/logged_out_user_access_verification.feature', 'Launch taxi service')
def test_logged_out_access_control(setup_browser):
    pass
