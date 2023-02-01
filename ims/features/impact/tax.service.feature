Feature: tax service

    Scenario: Tax task approve and tax list
        Given login to ims
		    And <tax-service> load page
            And create task
            And approve task
        When Do <approved-tax> to approved task
            And tax transaction list
        Then <datatable-scroll> screen shot by class name <tax> 

    Scenario: Tax service transaction 
        Given login to ims
		    And <tax-service> load page
            And create task
            And approve task                    
        When Do <approved-tax> to approved task
            And tax transaction
        Then <tax transaction> completed

    Scenario: Tax Service - decline reqeust
        Given login to ims
		    And <tax-service> load page
        When create task
        Then decline task 
        
