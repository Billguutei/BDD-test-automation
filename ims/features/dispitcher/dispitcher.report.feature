Feature: Dispitcher auto transaction report inquiry

    Scenario: Insert registered date and transfered account then click search
        Given login to ims
            And <dispitcher_report> load page
            And check page loaded <Тайлан лавлах>
        Then get report and take screenshot