Feature: bulk list

    Scenario: show bulk list
        Given login to ims
            And <bulk list> load page
            And check page loaded <Файлын жагсаалт>
        When <show> bulk list
        Then <table-responsive> screen shot by class name <bulk-list>
        
        #     And check page loaded <Салбарууд>
        # When <add> branch
        # Then <add branch> completed
        #     And check the table again <new>