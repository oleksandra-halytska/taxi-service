Feature: Login to Taxi Service website

  Scenario: Log in to Taxi Service web site and verify that logging process was successful
    When open login page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

  Scenario Outline: Verify that all the services are available for logged in user
    When open <page_name> page
    Then Car list text is available on cars page
    Examples:
      | page_name     |
      | cars          |
