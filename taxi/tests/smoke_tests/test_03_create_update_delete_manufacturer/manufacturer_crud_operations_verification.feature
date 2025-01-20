Feature: Verify that unauthorized users cannot access restricted pages

  Scenario: Launch taxi service
    When open 'login' page
    When the user enters valid credentials
    When the user submits the form
    Then the user should be redirected to the home page

    When open 'All manufacturers' page
    Then 'Manufacturer List' h1 is available on 'All manufacturers' page

    When click on 'Add manufacturer' link on 'All manufacturers' page
    When fill the 'Name*' field with 'Tarasova Irina' text on 'All manufacturers' page
    When fill the 'Country*' field with 'Ukraine' text on 'All manufacturers' page
    When click on 'Submit' button on 'All manufacturers' page
    Then 'Manufacturer List' h1 is available on 'All manufacturers' page