Feature: 1110

	Scenario: 1010 correction 1110
        Given login to ims
		    And <1010> load page
            And check page loaded <Бэлэн мөнгөний орлого>
			And <1010> transaction process <DEPOSIT_ACCOUNT>
        	And <income transaction> completed
		When <transaction list> load page
			And Search transaction with description
        	And approve task
		Then Do correction for <1010>
			And <correction> completed