Feature: mik-system loan account menu feature

  Scenario: add loan account positive
    Given login to ims
    And <mik-loan account> load page
    And check page loaded <Зээлийн данс бүртгэх>
    When press on add account
    Then <mikSystem xml add-information> completed

  Scenario: inquire loan account positive
    Given login to ims
    And <mik-loan account> load page
    And check page loaded <Зээлийн данс бүртгэх>
    Then inquired loan account should be in the table

    Scenario: delete loan account from the table positive
      Given login to ims
      And <mik-loan account> load page
      And check page loaded <Зээлийн данс бүртгэх>
      When delete loan account from the table
      Then <mikSystem loanAccount delete-loan-account> completed

  Scenario: loan account information downloand excel
    Given login to ims
    And <mik-loan account> load page
    And check page loaded <Зээлийн данс бүртгэх>
    Then mik-loan-account download excel

