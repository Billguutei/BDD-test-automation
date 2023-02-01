Feature: 1054

    Scenario: 1054 transaction positive
        Given login to ims
            And <1054> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <1054> transaction process <RECEIVING_ACCOUNT>
        Then <transfer transaction> completed

    Scenario: 1054 transaction decline request
        Given login to ims
            And <1054> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task
