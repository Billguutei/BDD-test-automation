Feature: 10400

    Scenario: 10400 inquiry positive
		Given login to ims
		    And <10400> load page
            And check page loaded <Зээлийн дансны лавлагаа>
        When <10400>-<1> multi window <LOAN_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <10400-1>

    Scenario: 10400 inquiry cancel to request
		Given login to ims
		    And <10400> load page
            And check page loaded <Зээлийн дансны лавлагаа>
        When <10400>-<1> multi window <LOAN_ACCOUNT>
            And create task
        Then  decline task
        Then <content> screen shot by class name <10400-cancel>