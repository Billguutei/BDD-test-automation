Feature: Card order reissue

    Scenario: Search by account number
        Given login to ims
		    And <card-reissue> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <reissue> account number
        # Then <search customer> completed
 
    Scenario:  address is  branch of recieve card
        Given login to ims
		    And <card-reissue> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <reissue> account number
        When <branch> fill fields of order reissue and renewal
        Then <reissue card> completed

    Scenario:  Address is  post of recieve card
        Given login to ims
		    And <card-reissue> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <reissue> account number
        When <post> fill fields of order reissue and renewal
        Then <reissue card> completed

    Scenario:  Fee is manual
        Given login to ims
		    And <card-reissue> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <reissue> account number
        When <fee-manaul> fill fields of order reissue and renewal
        Then <reissue card> completed
