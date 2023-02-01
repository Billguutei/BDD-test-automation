Feature: 14045

    Scenario: 14045 transaction positive
        Given login to ims
		    And <14045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
		When <14045> transaction process <LOAN_ACCOUNT>
		Then <transfer transaction> completed
    
    Scenario: 14045 transaction decline task positive
        Given login to ims
		    And <14045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task