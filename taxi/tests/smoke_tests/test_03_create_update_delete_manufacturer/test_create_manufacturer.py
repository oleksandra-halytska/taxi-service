import pytest
from pytest_bdd import scenarios
from pytest_bdd import when, then, parsers, scenario


# @pytest.mark.django_db(transaction=True)
# def main():
#     scenarios("./manufacturer_crud_operations_verification.feature")

@pytest.mark.django_db(transaction=True)
@scenario('manufacturer_crud_operations_verification.feature', 'Launch taxi service')
def test_launch_taxi_service():
    pass
