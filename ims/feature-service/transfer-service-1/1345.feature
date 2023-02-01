Feature: 1345

    Scenario: 1345 transaction positive
        Given login to ims
            And <1345> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <1345> transaction process <TIME_DEPOSIT_ACCOUNT>
        Then <income transaction> completed

    Scenario: 1345 transaction decline task positive
        Given login to ims
            And <1345> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task