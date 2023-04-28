# Created by emreisik at 4/20/23
Feature: Verify product details page opened and product name is correct

  Scenario: Search results show the right result
    Given Open main page
    When  Close the pop up
    When  Click on search icon in the header
    Then  Input into search field SPF
    Then  Verify results have SPF