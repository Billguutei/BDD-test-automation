Feature: 10450

    Scenario: 10450 inquiry positive
	    When login to ims
            And <10450> load page
            And check page loaded <Зээлийн дансны лавлагаа>
        Given <10450> fill field <LOAN_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <10450>

    Scenario: 10450 inquiry cancel to request
	    When login to ims
            And <10450> load page
            And check page loaded <Зээлийн дансны лавлагаа>
        Given <10450> fill field <LOAN_ACCOUNT>
            And create task
        Then decline task
        Then <page-container> screen shot <10450-cancel>