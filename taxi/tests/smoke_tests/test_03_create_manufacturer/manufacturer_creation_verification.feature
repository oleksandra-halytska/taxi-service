Feature: Verify that unauthorized users cannot access restricted pages

  Scenario: Launch taxi service
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page
