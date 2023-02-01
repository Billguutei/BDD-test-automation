Feature: Forex Feature

    Scenario: Approved deals
        Given login to ims
		    And <forex-deals> load page
            And check page loaded <Хэлцлийн дугаар>
        Then open approved deals