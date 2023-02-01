Feature: 20060

    Scenario: 20060 transaction positive
        Given login to ims
            And <20060> load page
            And check page loaded <Дотоодын бэлэн зарлага>
        When <20060> transaction process <GEND_ACCOUNT>
        Then <outcome transaction> completed