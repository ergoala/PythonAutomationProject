Feature: Login
  As a user
  I want to log in to the application
  So that I can access the products

  Background:
    Given the user is on the login page

  @smoke @login
  Scenario: Successful login
    When the user enters valid credentials
    Then the user should see the products page

  @regression @login
  Scenario: Login with invalid credentials
    When the user enters invalid credentials
    Then the user should see an error message
    And the error message should contain "Username and password do not match"

  @regression @login
  Scenario: Login with locked out user
    When the user enters locked out user credentials
    Then the user should see an error message
    And the error message should contain "locked out"

  @smoke @login
  Scenario: Login with empty fields
    When the user clicks the login button
    Then the user should see an error message
    And the error message should contain "Username is required"
