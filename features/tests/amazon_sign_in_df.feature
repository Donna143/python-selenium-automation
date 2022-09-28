# Created by thebe at 9/28/2022
Feature: Tests for sign in page

  Scenario: Sign in page opens when clicking Returns and Orders
    Given Open Amazon page
    When User clicks Returns & Orders
    Then Sign in page opens