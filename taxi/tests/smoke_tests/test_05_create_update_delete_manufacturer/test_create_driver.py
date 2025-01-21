from pytest_bdd import scenario


@scenario(
    'driver_crud_operations_verification.feature',
    'Verify that CRUD operations work for Driver object'
)
def test_driver_crud(setup_browser):
    pass
