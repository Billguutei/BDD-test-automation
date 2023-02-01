Feature: 440

    Scenario: 440 inquiry positive
        Given login to ims
            And <440> load page
            And check page loaded <Депозит лавлагаа>
        Given <440> fill field <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <440>