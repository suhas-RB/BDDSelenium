Feature: login feature
  Background: pre-condition
    Given browser is opened
    When we enter https://demo.actitime.com/login.do in address bar


    Scenario: valid login
      Given login page is displayed
      When we enter suhas in username
      And we enter manager in password
      And we click on login button
      Then home page should be displayed


    Scenario Outline: invalid login
      Given login page is displayed
      When we enter <un> in username
      And we enter <pwd> in password
      And we click on login button
      Then error msg should be displayed
      Examples:
        | un    | pwd      |
        | abc   | xyz      |
        | suhas | suhas123 |
