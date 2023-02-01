Feature: product

    Scenario: add product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <add> product
        Then <add product> completed
            And <search_added> product

    Scenario: search product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <search> product
        Then <datatable-scroll> screen shot by class name <product>

    Scenario: update product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <update> product
        Then <update product> completed
            And <search_updated> product

    Scenario: delete product positive
        Given login to ims
            And <access-product> load page
            And check page loaded <Нэр>
        When <delete> product
        Then <delete product> completed
            And <search_deleted> product
