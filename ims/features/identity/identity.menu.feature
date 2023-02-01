Feature: menu

    Scenario: add menu positive
        Given login to ims
            And <access-menu> load page
            And check page loaded <Цэсийн нэр>
        When <add> menu
        Then <add menu> completed

    Scenario: update menu positive
        Given login to ims
            And <access-menu> load page
            And check page loaded <Цэсийн нэр>
        When <update> menu
       Then <update menu> completed

    Scenario: open menu positive
        Given login to ims
            And <access-menu> load page
            And check page loaded <Цэсийн нэр>
        When <open> menu
        Then <panel.panel-flat> screen shot by class name <menu>

    Scenario: delete menu positive
        Given login to ims
            And <access-menu> load page
            And check page loaded <Цэсийн нэр>
        When <delete> menu
        Then <delete menu> completed