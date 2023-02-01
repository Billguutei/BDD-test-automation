Feature: 10440

    Scenario: 10440 inquiry positive
        When login to ims
            And <10400> load page
            And check page loaded <Зээлийн дансны лавлагаа>
        Given <10440> fill field <LOAN_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <10440>

    Scenario: 10440 inquiry cancel to request
        When login to ims
            And <10400> load page
            And check page loaded <Зээлийн дансны лавлагаа>
        Given <10440> fill field <LOAN_ACCOUNT>
            And create task
        Then decline task
        Then <page-container> screen shot <10440-cancel>
