Feature: Card order renewal

    Scenario: Search by account number
        Given login to ims
		    And <card-renewal> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <renewal> account number
        # Then <search customer> complete
 
    Scenario:  address is  branch of recieve card
        Given login to ims
		    And <card-renewal> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <renewal> account number
        When <branch> fill fields of order reissue and renewal
        Then <renewal card> completed

    Scenario:  Address is  post of recieve card
        Given login to ims
		    And <card-renewal> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <renewal> account number
        When <post> fill fields of order reissue and renewal
        Then <renewal card> completed

    Scenario:  Fee is manual
        Given login to ims
		    And <card-renewal> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <renewal> account number
        When <fee-manaul> fill fields of order reissue and renewal
        Then <renewal card> completed
