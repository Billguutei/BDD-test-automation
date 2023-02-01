 Feature: bulk branch list
 
    Scenario: show branch list
        Given login to ims
            And <bulk-branchlist> load page
        When check page loaded <Салбар №>
        Then <table> screen shot by class name <bulk-branchlist>