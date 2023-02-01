Feature: 1160

    Scenario: 1060 correction 1160 
        Given login to ims
            And <1060> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
            And <1060> transaction process <DEPOSIT_ACCOUNT>
            And <outcome transaction> completed
		When <transaction list> load page
			And Search transaction with description
        	And approve task
        Then Do correction for <1060>
            And <correction> completed


    