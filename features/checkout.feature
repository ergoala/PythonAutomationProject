Feature: Checkout
  As a logged in user
  I want to complete the checkout process
  So that I can purchase products

  Background:
    Given the user is logged in
    And the user has products in the cart

  @smoke @checkout
  Scenario: Complete checkout flow
    When the user goes to the cart
    And the user proceeds to checkout
    And the user fills in checkout information
    Then the order summary should be displayed
    When the user finishes the order
    Then the user should see the confirmation message

  @regression @checkout
  Scenario: Remove item from cart
    When the user goes to the cart
    Then the cart should contain 2 items
    When the user removes item 0 from the cart
    Then the cart should contain 1 item

  @regression @checkout
  Scenario: Checkout with missing data
    When the user goes to the cart
    And the user proceeds to checkout
    And the user clicks continue without filling information
    Then the user should see an error message
    And the error message should contain "First Name is required"
