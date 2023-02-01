Feature: 1043

    Scenario: 1043 transaction positive
        Given login to ims
            And <1043> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <1043> transaction process <DEPOSIT_ACCOUNT>
        Then <transfer transaction> completed
