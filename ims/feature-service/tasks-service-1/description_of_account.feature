Feature: Description of account

    Scenario: Decription of account menu by account positive
        When login to ims
        Then check home page loaded
        When open description of account menu
        Given search by account number
        Then <page-content> screen shot <description-of-account>

    Scenario: Description of account menu by register positive
        When login to ims
        Then check home page loaded
        When open description of account menu
        Given search by register number
        Then <page-content> screen shot <description-of-register>