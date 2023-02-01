Feature: 3060

    Scenario: 3060 transaction positive
        Given login to ims
            And <3060> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <3060> transaction process <CLOSE_ACCOUNT>
        Then <close transaction> completed
    
    Scenario: 3060 transaction decline task positive
        Given login to ims
            And <3060> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task