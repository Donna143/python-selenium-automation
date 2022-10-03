# Created by thebe at 9/28/2022
Feature: Tests for amazon cart

  Scenario: Amazon cart is empty
    Given Open Amazon page
    When Click on cart
    Then Amazon cart is empty


  Scenario:  Add product to cart
    Given Open Amazon page
    When Search for Little Women book
    And Click on first product
    And Click Add to Cart button
    Then Verify cart has 1 item(s)