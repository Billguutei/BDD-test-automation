Feature: 3045

    Scenario: 3045 transaction positive
        Given login to ims
            And <3045> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <3045> transaction process <CLOSE_ACCOUNT>
        Then <close transaction> completed

    Scenario: 3045 transaction decline task positive
        Given login to ims
            And <3045> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task