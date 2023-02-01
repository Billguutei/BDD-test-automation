Feature: 400

    Scenario: 400-1 inquiry positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<1> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-1>

    Scenario: 400-1 inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<1> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task

    Scenario: 400-2 inquiry positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<2> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-2>

    Scenario: 400-2 inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<2> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task

    Scenario: 400-3 inquiry positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<3> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-3>

    Scenario: 400-3 inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<3> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task

    Scenario: 400-5 inquiry positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<5> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-5>

    Scenario: 400-5 inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<5> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task

    Scenario: 400-7 inquiry positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<7> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-7>

    Scenario: 400-7 inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<7> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task

    Scenario: 400-P inquiry positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<P3> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-P>

    Scenario: 400-P inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<P> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task

    Scenario: 400-4 inquiry positive
        Given login to ims
        And <400> load page
            And check page loaded <Депозит лавлагаа>
        When <400>-<4> multi window <DEPOSIT_ACCOUNT>
            And create task
            And approve task
        Then <ui-dialog> screen shot <400-4>

    Scenario: 400-4 inquiry decline task positive
        Given login to ims
            And <400> load page
            And check page loaded <Депозит лавлагаа>
            And <400>-<4> multi window <DEPOSIT_ACCOUNT>
        When create task
        Then decline task