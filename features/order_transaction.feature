Feature: Order Transaction
  Test related to order transactions.

  Scenario Outline: Verify order details message is shown in details page
    Given Place the item order with <username> and <password> using the API
    And the user is on the landing page

    When  I Login to portal with <username> and <password>
    And Navigate to orders page
    And  Select the order with the correct order Id

    Then order message is successfully displayed

    Examples:
      | username                      | password            |
      | g.threepwood@melee.gov        | FJAA1983.rahul      |
