Feature: 14045

    Scenario: 14145 transaction positive
        Given login to ims
		    And <14045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
		    And <14045> transaction process <LOAN_ACCOUNT>
		    And <transfer transaction> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <14045>
            And <correction> completed

    Scenario: 14045 transaction decline task positive
        Given login to ims
		    And <14045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task