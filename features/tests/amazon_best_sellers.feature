# Created by thebe at 10/2/2022
Feature: Tests for Amazon Best Sellers page

  Scenario: Header has correct amount of links
    Given Open Amazon page
    When Click on Best Sellers
    Then Verify that header has 5 links


  Scenario: Correct page opens when clicking each header link
    Given Open Amazon page
    When Click on Best Sellers
    Then Click each header link and verify correct page opens
