# Created by thebe at 9/28/2022
Feature: Tests for Amazon search

#  Scenario: User can search for coffee
#    Given Open Amazon page
#    When Search for coffee
#    Then Search results for "coffee" are shown
#
#
#  Scenario: User can search for mug
#    Given Open Amazon page
#    When Search for mug
#    Then Search results for "mug" are shown


  Scenario Outline:
    Given Open Amazon page
    When Search for <product>
    Then Search results for <search_result> are shown
    Examples:
    | product       | search_result      |
    | coffee        | "coffee"           |
    | mug           | "mug"              |
    | dress         | "dress"            |

