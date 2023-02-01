Feature: role group

    Scenario: add role group positive
        Given login to ims
            And <access-group> load page
            And check page loaded <Бүтээгдэхүүний Эрх-үүд>
        When <add> group
        Then <add group> completed

    Scenario: open role group positive
        Given login to ims
            And <access-group> load page
            And check page loaded <Бүтээгдэхүүний Эрх-үүд>
        When <open> group
        Then <panel-body> screen shot by class name <group>

    Scenario: update role group positive
        Given login to ims
            And <access-group> load page
            And check page loaded <Бүтээгдэхүүний Эрх-үүд>
        When <update> group
        Then <update group> completed

    Scenario: delete role group positive
        Given login to ims
            And <access-group> load page
            And check page loaded <Бүтээгдэхүүний Эрх-үүд>
        When <delete> group
        Then <delete group> completed