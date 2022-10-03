# Created by thebe at 10/2/2022
Feature: Tests for Amazon main page

  Scenario: Hamburger menu is present
    Given Open Amazon page
    Then Verify hamburger menu is present


  Scenario: Footer has correct amount of links
    Given Open Amazon page
    Then Verify that footer has 38 links