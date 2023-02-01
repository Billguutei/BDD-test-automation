Feature: Search by card with account and cif and card number

    Scenario: Search by account
        Given login to ims
		    And <card-search> load page
            And check page loaded <Харилцагч хайх>
        When Search for a card <account_number>
        Then check page loaded <Картын дугаар>
        Then <table-responsive> screen shot by class name <card_list_by_account>

    Scenario: Search by card number
        Given login to ims
		    And <card-search> load page
            And check page loaded <Харилцагч хайх>
        When Search for a card <card_number>
        Then check page loaded <Картын дугаар>
        Then <table-responsive> screen shot by class name <card_list_by_card>

    Scenario: Search by cif number
        Given login to ims
		    And <card-search> load page
            And check page loaded <Харилцагч хайх>
        When Search for a card <cif_number>
        Then check page loaded <Картын дугаар>
        Then <table-responsive> screen shot by class name <card_list_by_cif>
