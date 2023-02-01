Feature: Organization registration configuration
  Scenario: Inquire contract history
    Given login to ims
    And <organization list> load page
    And check page loaded < Байгууллагын жагсаалт >
    When <inquire contract> on table
    #Then inquire organization contract completed

  Scenario: Inquire contract by condition
    Given login to ims
    And <organization registry> load page
    And check page loaded < Байгууллагын жагсаалт >
    When <inquire conditionally> on table
    #Then inquire conditionally completed

  Scenario: Inquire contract by status
    Given login to ims
    And <organization registry> load page
    And check page loaded < Байгууллагын жагсаалт >
    When <inquire by status> on table
    #Then inquire by status completed

  Scenario: print a contract
    Given login to ims
    And <organization registry> load page
    And check page loaded < Байгууллагын жагсаалт >
    When <print a contract> on table
    #Then not print save pdf completed
