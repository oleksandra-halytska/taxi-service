Feature: Verify that authorized users have access to the restricted pages

  @smoke
  Scenario: Log in to Taxi Service web site and verify that logging process was successful
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

    When open 'All cars' page
    Then 'Car List' h1 is available on 'All cars' page

    When open 'All drivers' page
    Then 'Driver List' h1 is available on 'All drivers' page

    When open 'All manufacturers' page
    Then 'Manufacturer List' h1 is available on 'All manufacturers' page
