Feature: GET
  Scenario: Retrieve a list of users
    Given mock api is running
    When request to a server was successfully processed get users
    Then validate user data retrieval