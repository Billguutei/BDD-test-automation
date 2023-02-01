Feature: Дэвсгэртийн жагсаалт нээх
    Scenario: Open cash drawer
        Given login to ims
		    And <Exchange> load page
            And check page loaded <Гүйлгээний жагсаалт>
		Then <Open_CashList> process