Feature: 60450

    Scenario: 60450 inquiry positive
		When login to ims
		    And <60450> load page
            And check page loaded <Харилцагчийн лавлагаа>
        Given <60450> fill field <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <tabbable> screen shot <60450>