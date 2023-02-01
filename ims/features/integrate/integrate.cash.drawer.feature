Feature: Дэвсгэртийн тоо ширхэг-ийг солих

    Scenario: Exchange in cash drawer
        Given login to ims
		    And <Exchange> load page
		Then <Change_banknotes> process
	