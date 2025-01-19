Feature: Verify that authorized users have access to the restricted pages

  Scenario: Log in to Taxi Service web site and verify that logging process was successful
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

  Scenario: Verify that all the services are available for logged in user
    When open '<page_name>' page
    Then '<expected_text>' h1 is available on '<page_name>' page
    Examples:
      | page_name         | expected_text     |
      | All cars          | Car List          |
      | All drivers       | Driver List       |
      | All manufacturers | Manufacturer List |
