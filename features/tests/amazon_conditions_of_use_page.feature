# Created by thebe at 10/18/2022
Feature: Tests for Conditions of Use page

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original


