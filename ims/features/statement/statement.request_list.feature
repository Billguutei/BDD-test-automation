Feature: request

    Scenario: request <Депозит дансны хуулга> inquiry positive
        Given login to ims
            And <request> load page
            And check page loaded <Хүсэлтийн жагсаалт>
        When <Депозит дансны хуулга> multi window
        Then <table-responsive> screen shot by class name <request-1>

    Scenario: request <Депозит дансны хуулга> inquiry positive
        Given login to ims
            And <request> load page
            And check page loaded <Хүсэлтийн жагсаалт>
        When <Депозит дансны хуулга> multi window
        Then <table-responsive> screen shot by class name <request-1>