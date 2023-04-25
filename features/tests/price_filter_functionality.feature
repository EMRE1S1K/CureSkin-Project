# Created by emreisik at 4/25/23
Feature: Verify Price filter Functionality

  Scenario: Verify Price filter Functionality
    Given Open cureskin homepage
    When Close the pop up
    When Click on Shop All section
    Then Adjust the Price Filter such that there is a change in number of products
    Then Verify that number of products changes
    Then Verify that products displayed are within the Price filter
