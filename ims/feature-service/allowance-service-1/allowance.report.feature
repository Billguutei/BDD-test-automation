Feature: Search allowance report user
  Scenario: insert right date an click search button
    Given login to ims
    And <allowance userReport> load page
    And check page loaded <Нөхөн олголтын тайлан>
    When download search by user report