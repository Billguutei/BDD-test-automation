Feature: Салбарын нэгтгэсэн дүн Хайлт хийх/ Хэвлэх/ PDF - ээр татаж авах

    #Scenario: 1010 transaction positive
    #    Given login to ims
	#	    And <1010> load page
    #        And check page loaded <Бэлэн мөнгөний орлого>
	#	When <1010> transaction process
    #    Then <income transaction> completed

    Scenario: Login and Search Integrated Amount
        Given login to ims
            And <Branch_IntegratedAmount> load page
        Then <Search> Integrated Amount that day
        	
    #Scenario: Login and Download PDF of Integrated Amount
    #    Given login to ims
    #          And <Branch_IntegratedAmount> load page
    #    Then <Download> Integrated Amount that day
    
    #Scenario: Login and Print Integrated Amount
    #    Given login to ims
    #        And <Branch_IntegratedAmount> load page
    #    Then <Print> Integrated Amount that day
	
	