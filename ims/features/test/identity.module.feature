Feature: module

    Scenario: add module positive
        Given login to ims
            And <access-module> load page
            And check page loaded <Нэр>
        When <add> module
        Then <add module> completed
            And <search_added> module

    Scenario: search module positive
        Given login to ims
            And <access-module> load page
            And check page loaded <Нэр>
        When <search> module
        Then <datatable-scroll> screen shot by class name <module>

    Scenario: update module positive
        Given login to ims
            And <access-module> load page
            And check page loaded <Нэр>
        When <update> module
        Then <update module> completed
            And <search_updated> module

    Scenario: delete module positive
        Given login to ims
            And <access-module> load page
            And check page loaded <Нэр>
        When <delete> module
        Then <delete module> completed
            And <search_deleted> module