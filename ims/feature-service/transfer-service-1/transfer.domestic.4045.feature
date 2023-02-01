Feature: 4045

    Scenario: 4045 transaction positive
        Given login to ims
		    And <4045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
		When <4045> transaction process <INTERNAL_ACCOUNT>
		Then <transfer transaction> completed
    
    Scenario: 4045 transaction decline task positive
        Given login to ims
		    And <4045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task