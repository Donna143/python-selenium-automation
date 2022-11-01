# Created by thebe at 9/28/2022
Feature: Tests for Amazon search

  Scenario: User can search for coffee
    Given Open Amazon page
    When Search for coffee
    Then Search results for "coffee" are shown
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


Scenario: Verify that user can see product names and images
  Given Open Amazon page
  When Search for coffee
  Then Verify that every product has a name and an image


Scenario Outline: User can select and search in a department
  Given Open Amazon page
  When Select department by value <value>
  And Search for Faust
  Then Verify <department> department is selected
  Examples:
  |value      |department   |
  |stripbooks |books        |
  |audible    |audible      |


Scenario: User can select and search in a department
  Given Open Amazon page
  When Select department by value digital-music
  And Search for Hozier
  Then Verify dmusic department is selected
