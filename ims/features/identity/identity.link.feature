Feature: link endpoint

    Scenario: add endpoint positive
        Given login to ims
            And <access-connection> load page
            And check page loaded <Модуль-иар Холбоосыг шүүх:>
        When <add> endpoint
        Then <identityService endpoint add> completed

    Scenario: edit endpoint positive
        Given login to ims
            And <access-connection> load page
            And check page loaded <Модуль-иар Холбоосыг шүүх:>
        When inquire endpoint in table by <testName>
            And <edit> endpoint
        Then <identityService endpoint edit> completed

    Scenario: inquire endpoint positive
        Given login to ims
            And <access-connection> load page
            And check page loaded <Модуль-иар Холбоосыг шүүх:>
        When inquire endpoint in table by <editedTestName>
        Then inquire endpoint completed

    Scenario: change status of a connection positive
        Given login to ims
            And <access-connection> load page
            And check page loaded <Модуль-иар Холбоосыг шүүх:>
        When inquire endpoint in table by <editedTestName>
            And <change> status
        Then <identityService endpoint change> completed

    Scenario: delete endpoint positive
        Given login to ims
            And <access-connection> load page
            And check page loaded <Модуль-иар Холбоосыг шүүх:>
        When inquire endpoint in table by <editedTestName>
            And <delete> endpoint
        Then <delete endpoint> completed
