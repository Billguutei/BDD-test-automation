Feature: Дэвсгэртийн жагсаалт нээх
    Scenario: Open cash drawer
        Given login to ims
		    And <Exchange> load page
		Then <Open_CashList> process