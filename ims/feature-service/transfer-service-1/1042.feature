Feature: 1042

    Scenario: 1042 transaction positive
        Given login to ims
            And <1042> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
            And approve task
        When <1042> transaction process <RECEIVING_ACCOUNT>
        Then <transfer transaction> completed

    Scenario: 1042 transaction cancel request
        Given login to ims
            And <1042> load page
            And check page loaded <Ажилтны хурууны хээ уншуулах талбар>
            And create task
        Then approve task
        Then <content> screen shot by class name <1042-decline>
