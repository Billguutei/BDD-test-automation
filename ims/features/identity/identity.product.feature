Feature: product

    Scenario: add product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <add> product
        Then <add product> completed
            And <search_added> module

    Scenario: search product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <search> product
        Then <datatable-scroll> screen shot by class name <product>

    Scenario: delete product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <delete> product
        Then <delete product> completed
            And <search_deleted> product

    Scenario: add product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <add> product
        Then <add product> completed
            And <search_added> module

    Scenario: update product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <update> product
        Then <update product> completed
            And <search_updated> product
