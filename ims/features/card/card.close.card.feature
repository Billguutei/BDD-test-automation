Feature: Card close

    Scenario: Search by account number
        Given login to ims
		    And <card-close> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <close> account number
        Then check page loaded <Картын дугаар>

    Scenario: Close to card
        Given login to ims
		    And <card-close> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <close> account number
        When Select the closing card
        Then <close card> completed
