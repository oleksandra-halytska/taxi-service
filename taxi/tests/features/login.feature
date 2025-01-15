Feature: Login Page

  Scenario: Successful login with valid credentials
    When opens login page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page
