import pytest
from pytest_bdd import scenario


@pytest.mark.django_db
@scenario('logged_out_user_access_verification.feature', 'Launch taxi service')
def test_logged_out_access_control(setup_browser):
    pass
