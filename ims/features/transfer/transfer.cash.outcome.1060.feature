Feature: 1060

    Scenario: 1060 transaction positive
        Given login to ims
            And <1060> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <1060> transaction process <DEPOSIT_ACCOUNT>
        Then <outcome transaction> completed

    Scenario: 1060 transaction decline task positive
        Given login to ims
            And <1060> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task