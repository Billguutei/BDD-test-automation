Feature: Close loan account

    Scenario: 3045 correction 3145 positive 
        Given login to ims
            And <3045> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
            And <3045> transaction process <CLOSE_ACCOUNT>
            And <close transaction> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <3045>
            And <correction> completed

    Scenario: 3145 correction  cancel request
        Given login to ims
            And <3045> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
        When create task
        Then decline task
