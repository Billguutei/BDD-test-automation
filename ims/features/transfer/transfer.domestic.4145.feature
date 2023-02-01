Feature: 4145

    Scenario: 4045 correction 4145 positive
        Given login to ims
		    And <4045> load page
		    And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
		    And <4045> transaction process <INTERNAL_ACCOUNT>
		    And <transfer transaction> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <4045>
            And <correction> completed
