# Created by thebe at 10/12/2022
Feature: Tests for product page

#  Scenario: User can select colors
#    Given Open Amazon product B07MNHBRCJ page
#    Then Verify user can click through colors

  Scenario: User can select colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through colors

  Scenario: User can see New Arrivals options
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user sees New Arrival options


