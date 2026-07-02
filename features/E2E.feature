Feature: End to End - Complete Purchase Flow
  As a user
  I want to complete a full purchase
  So that I can buy products from the store

  @e2e @smoke
  Scenario: Complete purchase flow - Happy Path
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should see the products page
    When the user adds item 0 to the cart
    And the user adds item 1 to the cart
    And the user goes to the cart
    Then the cart should contain 2 items
    When the user proceeds to checkout
    And the user fills in checkout information
    Then the order summary should be displayed
    When the user finishes the order
    Then the user should see the confirmation message
    And the confirmation message should contain "Thank you for your order"

  @e2e @regression
  Scenario: Purchase flow with item removal
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should see the products page
    When the user adds item 0 to the cart
    And the user adds item 1 to the cart
    And the user adds item 2 to the cart
    And the user goes to the cart
    Then the cart should contain 3 items
    When the user removes item 1 from the cart
    Then the cart should contain 2 items
    When the user proceeds to checkout
    And the user fills in checkout information
    When the user finishes the order
    Then the user should see the confirmation message

  @e2e @regression
  Scenario: Purchase flow - verify product names in cart
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should see the products page
    When the user adds "Sauce Labs Backpack" to the cart
    And the user goes to the cart
    Then "Sauce Labs Backpack" should be in the cart
    When the user proceeds to checkout
    And the user fills in checkout information
    Then the order summary should be displayed
    When the user finishes the order
    Then the user should see the confirmation message
