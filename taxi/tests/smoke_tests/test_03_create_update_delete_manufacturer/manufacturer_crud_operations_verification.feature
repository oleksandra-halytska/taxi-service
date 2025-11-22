Feature: Verify that CRUD operations work for Manufacturer object

  @smoke
  Scenario: Verify that CRUD operations work for Manufacturer object
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

    When open 'All manufacturers' page
    Then 'Manufacturer List' h1 is available on 'All manufacturers' page

    When click on 'Add manufacturer' link on 'All manufacturers' page
    When fill the 'Name*' field with 'iRINA' text on 'All manufacturers' page
    When fill the 'Country*' field with 'ukr' text on 'All manufacturers' page
    When click on 'Submit' button on 'All manufacturers' page
    Then 'Manufacturer List' h1 is available on 'All manufacturers' page

    When Update object: 'iRINA ukr' on 'All manufacturers' page with 'Irina Ukraine'
    When Delete object: 'Irina Ukraine' on 'All manufacturers' page
    Then 'Delete manufacturer' h1 is available on 'All manufacturers' page
    Then 'Are you sure, that you want' p is available on 'All manufacturers' page
    When click on 'delete' button on 'All manufacturers' page
    Then 'There are no manufacturers in the service.' p is available on 'All manufacturers' page
