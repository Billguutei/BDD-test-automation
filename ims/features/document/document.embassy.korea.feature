Feature: Visa account statement at the Embassy


    Scenario:  Visa account statement at the Embassy of Korea - cancel request
        Given login to ims
		    And <document-embassyKorea> load page
            And create task
        Then  decline task
        Then <decline task> completed

    Scenario:  Visa account statement at the Embassy of Korea - approve
        Given login to ims
		    And <document-embassyKorea> load page
            And create task
            And approve task

    Scenario:  Visa account statement at the Embassy of Korea
    #БНСУ-н виз хүсэгчдийн дансны хуулганы хураангуй маягт авах үйлчилгээ
        Given login to ims
		    And <document-embassyKorea> load page
            And create task
            And approve task
        When Do <approved-embassyKorea> to approved task
        Then <БНСУ-н виз хүсэгчдийн дансны хуулганы хураангуй маягт авах үйлчилгээ> choose type of embassy
        Then <page-container> screen shot by class name <screen-embassyKorea>
