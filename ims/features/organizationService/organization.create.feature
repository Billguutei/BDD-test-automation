Feature: Create Organization registration
  Scenario: Create general conditions ерөнхий нөхцөл
    Given login to ims
    And <organization registry create> load page
    And check page loaded <Байгууллагын ерөнхий мэдээлэл>
    When <general conditions> conditionally
    Then <create generalNotif> completed

  Scenario: Create special conditions-тусгай нөхцөл
    Given login to ims
      And <organization registry create> load page
      And check page loaded <Байгууллагын ерөнхий мэдээлэл>
    When <special conditions> conditionally
    Then <create specialNotif> completed

  Scenario: Create pay transfer-цалин дамжуулах
    Given login to ims
    And <organization registry create> load page
    And check page loaded <Байгууллагын ерөнхий мэдээлэл>
    When <pay transfer> conditionally
    Then <create paytransferNotif> completed
