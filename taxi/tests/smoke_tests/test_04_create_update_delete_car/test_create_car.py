from pytest_bdd import scenario


@scenario(
    '../test_04_create_update_delete_car/car_crud_operations_verification.feature',
    'Verify that CRUD operations work for Car object'
)
def test_car_crud(setup_browser, create_manufacturer):
    pass
