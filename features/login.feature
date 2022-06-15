Feature: login feature
  Background: pre-condition
    Given browser is opened
    When we enter https://demo.actitime.com/login.do in address bar


    Scenario: valid login
      Given login page is displayed
      When we enter admin in username
      And we enter manager in password
      And we click on login button
      Then home page should be displayed