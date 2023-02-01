Feature: 3160

    Scenario: 3060 correction 3160 positive
        Given login to ims
            And <3060> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
            And <3060> transaction process <CLOSE_ACCOUNT>
            And <close transaction> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <3060>
            And <correction> completed