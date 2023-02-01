Feature: Prepare and Print Deposit Account Transaction Statement

    #Scenario: Search Fullname and prepare statements
    #    Given login to ims
    #        And <statement> load page
    #        And create task
    #    When approve task
    #    Then customer search by <name>

    Scenario: Login and depAccStatement page
        Given login to ims
            And <statement> load page
            And create task
        When approve task
        Then <DEPOSIT_ACCOUNT> search by <account>

    #Scenario: Deposit Account Limited Statement Negative TC
    #    Given login to ims
    #        And <statement> load page
    #        And create task
    #    When approve task
    #    Then Limited Statement