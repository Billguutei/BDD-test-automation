Feature: 1360

    Scenario: 1360 transaction positive
        Given login to ims
            And <1360> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <1360> transaction process <TIME_DEPOSIT_ACCOUNT>
        Then <income transaction> completed

    Scenario: 1360 transaction decline task positive
        Given login to ims
            And <1360> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task