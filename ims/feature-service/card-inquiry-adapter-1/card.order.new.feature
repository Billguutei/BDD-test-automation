Feature: Search by account number

    Scenario: Search by account
        Given login to ims
		    And <card-orderOfNewCard> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <new-card> account number
        Then <content> screen shot by class name <searchCustomer>

    Scenario: Card order new card,  card fee is manual
        Given login to ims
		    And <card-orderOfNewCard> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <new-card> account number
        When <fee-manaul> fill fields of order new card 
        Then <order card> completed

    Scenario: Card order new card,  card fee is auto
        Given login to ims
		    And <card-orderOfNewCard> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <new-card> account number
        When <branch> fill fields of order new card 
        Then <order card> completed

    Scenario: Card order new card, address of  Receive a card is post  
        Given login to ims
		    And <card-orderOfNewCard> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <new-card> account number
        When <post> fill fields of order new card
        Then <order card> completed
    
        Scenario: Card order new card, address of  Receive a card is branch 
        Given login to ims
		    And <card-orderOfNewCard> load page
            And check page loaded <Харилцагч хайх>
        When Search for a customer by <new-card> account number
        When <branch> fill fields of order new card 
        Then <order card> completed
