# Created by thebe at 10/12/2022
Feature: Sign in test cases

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign in page opened


  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 5 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears



