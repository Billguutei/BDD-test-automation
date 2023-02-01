Feature: 20160

    Scenario: 20060 correction 20160 positive
        Given login to ims
            And <20060> load page
            And check page loaded <Дотоодын бэлэн зарлага>
            And <20060> transaction process <GEND_ACCOUNT>
            And <outcome transaction> completed
        When <transaction list> load page
            And Search transaction with description
            And approve task
        Then Do correction for <20060>
            And <correction> completed

       
    Scenario: 20060 transaction decline task positive
        Given login to ims
            And <20060> load page
            And check page loaded <Дотоодын бэлэн зарлага>
            And <20060> transaction process <GEND_ACCOUNT>
            And <outcome transaction> completed
        When <transaction list> load page
            And Search transaction with description
        Then decline task