Feature: 11055

    Scenario: 11055 transaction positive
        Given login to ims
            And <11055> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <11055> transaction process <LOAN_ACCOUNT_TO_DEP>
        Then <transfer loan> completed
        

