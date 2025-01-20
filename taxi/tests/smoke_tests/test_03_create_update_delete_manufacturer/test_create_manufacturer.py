from pytest_bdd import scenario


@scenario(
    'manufacturer_crud_operations_verification.feature',
    'Verify that CRUD operations work for Manufacturer object'
)
def test_manufacturer_crud(setup_browser):
    pass
