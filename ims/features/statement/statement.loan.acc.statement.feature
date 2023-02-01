Feature: Prepare and Print Loan Account Transaction Statement

    Scenario: Login and loanpayment page
        Given login to ims
            And <loan_statement> load page
            And create task
        When approve task
        Then <LOAN_ACCOUNT> search by <account>

        #Then fill fields of loanstatement

        
    #Scenario: Search Fullname and prepare statements
    #    Given login to ims
    #        And <statement> load page
    #        And create task
    #    When approve task
    #    Then customer search by <name>
