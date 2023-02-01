Feature: 20450 gen transaction inquiry

    Scenario: 20450 inquiry positive
		When login to ims
		    And <20450> load page
            And check page loaded <Дотоодын дансны лавлагаа>
        Given <20450> fill field <GEND_ACCOUNT>
        Then <table> screen shot by class name <20450>