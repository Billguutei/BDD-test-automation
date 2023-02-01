Feature: 21046

     Scenario: 21046 transaction positive AUD-MNT
        Given login to ims
            And <21046> load page
            And check page loaded <Валют арилжаа>
            And <AUD-MNT> transaction process
            And <currency exchange> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <21046>
            And <correction> completed

