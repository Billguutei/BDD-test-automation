Feature: Хэрэглэгчийн нэгтгэсэн дүн Хайлт хийх/ Хэвлэх/ PDF - ээр татаж авах

    Scenario: Login and Search Integrated Amount
        Given login to ims
            And <User_IntegratedAmount> load page
        Then <Search> Integrated Amount that day
        	
    #Scenario: Login and Download PDF of Integrated Amount
    #    Given login to ims
    #          And <User_IntegratedAmount> load page
    #    Then <Download> Integrated Amount that day
    
    #Scenario: Login and Print Integrated Amount
    #    Given login to ims
    #        And <User_IntegratedAmount> load page
    #    Then <Print> Integrated Amount that day
	
	