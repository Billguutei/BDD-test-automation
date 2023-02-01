Feature: 20010

    Scenario: 20010 transaction positive
        Given login to ims
		    And <20010> load page
            And check page loaded <Дотоодын бэлэн орлого>
		When <20010> transaction process <GEND_ACCOUNT>
        Then <income transaction> completed