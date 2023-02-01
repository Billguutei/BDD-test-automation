Feature: Change the card transaction limit

    # Scenario: Search by account number
    #     Given login to ims
	# 	    And <card-changeLimitofTranaction> load page
    #         And check page loaded <Харилцагч хайх>
    #     When Search for a customer by <changeLimitofTranaction> account number
    #     Then check page loaded < Картын дугаар сонгох >

    Scenario: Change limit of cash transaction
        Given login to ims
		    And <card-changeLimitofTranaction> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <changeLimitofTranaction> account number
        Then check page loaded < Картын дугаар сонгох >
        When <cash> fill fields and go transaction
        Then <change-limit card> completed

    Scenario: Change limit of non-cash transaction
        Given login to ims
		    And <card-changeLimitofTranaction> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <changeLimitofTranaction> account number
        Then check page loaded < Картын дугаар сонгох >
        When <non-cash> fill fields and go transaction
        Then <change-limit card> completed

#We need correct message of notification 
