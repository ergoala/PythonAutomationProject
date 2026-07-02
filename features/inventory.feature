Feature: Inventory
  As a logged in user
  I want to view and interact with products
  So that I can add items to my cart

  Background:
    Given the user is logged in
    And the user is on the inventory page

  @smoke @inventory
  Scenario: Page title is displayed
    Then the page title should be "Products"

  @regression @inventory
  Scenario: Products list is displayed
    Then the products list should contain 6 items

  @regression @inventory
  Scenario: Product names are displayed
    Then the products should have names
    And "Sauce Labs Backpack" should be in the product list

  @regression @inventory
  Scenario: Product prices are displayed
    Then the products should have prices
    And all prices should start with "$"

  @smoke @inventory
  Scenario: Add product to cart
    When the user adds item 0 to the cart
    Then the cart should contain 1 item

  @regression @inventory
  Scenario: Add multiple products to cart
    When the user adds item 0 to the cart
    When the user adds item 1 to the cart
    When the user adds item 2 to the cart
    Then the cart should contain 3 items
