Feature: Definition of Deposit Account 

    Scenario:  Definition of non-standard account balance
        Given login to ims
		    And <document-definitionDeposit> load page
            And create task
            And approve task
        When Do <approved-definitionDeposit> to approved task
        Then <Стандарт бус дансны үлдэгдэлгүй тодорхойлолт> choose type of definition
        Then <page-container> screen shot by class name <Definition of non-standard account balance>
    
    Scenario: Non-standard definition 
        Given login to ims
		    And <document-definitionDeposit> load page
            And create task
            And approve task
        When Do <approved-definitionDeposit> to approved task
        Then <Стандарт бус тодорхойлолт > choose type of definition
        Then <page-container> screen shot by class name <Non-standard definition>

    Scenario: Definition without standard account balance
        Given login to ims
		    And <document-definitionDeposit> load page
            And create task
            And approve task
        When Do <approved-definitionDeposit> to approved task
        Then <Стандарт дансны үлдэгдэлгүй тодорхойлолт> choose type of definition
        Then <page-container> screen shot by class name <Definition without standard account balance>
    
    Scenario: Standard definition
        Given login to ims
		    And <document-definitionDeposit> load page
            And create task
            And approve task
        When Do <approved-definitionDeposit> to approved task
        Then <Стандарт тодорхойлолт> choose type of definition
        Then <page-container> screen shot by class name <Standard definition>

    Scenario: Decline task
        Given login to ims
		    And <document-definitionDeposit> load page
            And create task
        Then decline task
