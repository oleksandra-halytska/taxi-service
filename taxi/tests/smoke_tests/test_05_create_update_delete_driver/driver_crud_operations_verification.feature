Feature: Verify that CRUD operations work for Driver object

  Scenario: Verify that CRUD operations work for Driver object
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

    When open 'All drivers' page
    Then 'Driver List' h1 is available on 'All drivers' page

    When click on 'Add driver' link on 'All drivers' page
    When fill the 'Name*' field with 'iRINA' text on 'All drivers' page
    When fill the 'License number*' field with 'AAA45678' text on 'All drivers' page
    When fill the 'First name' field with 'Irina' text on 'All drivers' page
    When fill the 'Last name' field with 'Tarasova' text on 'All drivers' page
    When fill the 'Password*' field with 'test_password' text on 'All drivers' page
    When fill the 'Password confirmation*' field with 'test_password' text on 'All drivers' page
    When click on 'Submit' button on 'All drivers' page
    Then 'Driver List' h1 is available on 'All drivers' page

    When Update object: 'Tarasova AAA45678' on 'All drivers' page with 'BBB45678'
    When Delete object: 'Tarasova BBB45678' on 'All drivers' page
    Then 'Delete driver' h1 is available on 'All drivers' page
    Then 'Are you sure, that you want' p is available on 'All drivers' page
    When click on 'delete' button on 'All drivers' page
