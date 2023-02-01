Feature: 1010

    Scenario: 1010 transaction positive
        Given login to ims
		    And <1010> load page
            And check page loaded <Бэлэн мөнгөний орлого>
		When <1010> transaction process <DEPOSIT_ACCOUNT>
        Then <income transaction> completed