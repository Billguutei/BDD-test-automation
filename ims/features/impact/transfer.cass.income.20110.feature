Feature: 20110

    Scenario: 20010 correction 20110 positive
        Given login to ims
		    And <20010> load page
            And check page loaded <Дотоодын бэлэн орлого>
		    And <20010> transaction process <GEND_ACCOUNT>
            And <income transaction> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <20010>
            And <correction> completed

    