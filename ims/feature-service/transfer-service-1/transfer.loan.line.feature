Feature: 11044

    Scenario: 11044 loan line
        Given login to ims
            And <11044> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <11044> transaction process <LOAN_ACCOUNT>
        Then <transfer loan> completed
        

