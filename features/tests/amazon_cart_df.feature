# Created by thebe at 9/28/2022
Feature: Tests for amazon cart

  Scenario: Amazon cart is empty
    Given Open Amazon page
    When User clicks cart
    Then Amazon cart is empty