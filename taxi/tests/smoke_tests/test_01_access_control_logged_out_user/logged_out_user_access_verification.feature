Feature: Verify that unauthorized users cannot access restricted pages

  @smoke
  Scenario: Launch taxi service
    When open 'login' page
    Then 'Please login to see this page' p is available on 'login' page

    When open 'All cars' page
    Then 'Please login to see this page' p is available on 'All cars' page

    When open 'All drivers' page
    Then 'Please login to see this page' p is available on 'All drivers' page

    When open 'All manufacturers' page
    Then 'Please login to see this page' p is available on 'All manufacturers' page
