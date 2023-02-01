Feature: Organization registration Configuration
  # Scenario: Save organization configuration
  #   Given login to ims
  #   And <organization registry> load page
  #   And check page loaded <Тохиргоо>
  #   When <save configuration> in table
  #   Then <save settings> completed

  Scenario: Add configuratoin of organization registraion
    Given login to ims
    And <organization registry> load page
    And check page loaded <Тохиргоо>
    When <add configuration> in table
    Then <save settings> completed

  # Scenario: delete configuratoin of organization registraion
  #   Given login to ims
  #   And <organization registry> load page
  #   And check page loaded <Тохиргоо>
  #   When <delete configuration> in table
    # Then <delete settings> completed
