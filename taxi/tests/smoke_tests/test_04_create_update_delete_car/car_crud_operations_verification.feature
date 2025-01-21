Feature: Verify that CRUD operations work for Car object

  Scenario: Verify that CRUD operations work for Car object
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

    When open 'All cars' page
    Then 'Car List' h1 is available on 'All cars' page

    When click on 'Add car' link on 'All cars' page
    When fill the 'Model*' field with 'NisSan' text on 'All cars' page
    When Select 'test_manufacturer country' option from 'Manufacturer*' options on 'All cars' page
    When Check 'test' object on 'All cars' page
    When click on 'Submit' button on 'All cars' page
    Then 'Car List' h1 is available on 'All cars' page

    When Update object: 'NisSan test_manufacturer' on 'All cars' page with 'Nissan'
    When Delete object: 'Nissan	test_manufacturer' on 'All cars' page
    Then 'Delete car' h1 is available on 'All cars' page
    Then 'Are you sure, that you want' p is available on 'All cars' page
    When click on 'delete' button on 'All cars' page
    Then 'There are no cars in the taxi service' p is available on 'All cars' page
