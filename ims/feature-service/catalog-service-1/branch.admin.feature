Feature: branch-admin-menu

    Scenario: add branch to the table
        Given login to ims
            And <branch admin> load page
            And check page loaded <Салбарууд>
        When <add> branch
        Then <add branch> completed
            And check the table again <new>

    Scenario: edit branch information in the table
        Given login to ims
            And <branch admin> load page
            And check page loaded <Салбарууд>
        When <edit> branch
        Then <edit branch> completed
            And check the table again <edited>

    Scenario: delete branch from the table
        Given login to ims
            And <branch admin> load page
            And check page loaded <Салбарууд>
        When <delete> branch in admin menu
        Then <delete> branch
            And check the table again <deleted>