Feature: Search allowance by customer register
  Scenario: insert right register of customer then click search button
    Given login to ims
    And <allowance_customer> load page
    And check page loaded <Татан буусан банкны нөхөн олговор>
    When insert value
    #Then take screenshot successfully