Feature: Organization registration Supervisors Албан тушаалтан жагсаалт
  Scenario: Add New Supervisor
    Given login to ims
    And <organization registry supList> load page
    And check page loaded < Баталгаажуулах албан тушаалтан жагсаалт >
    When <add> supervisor to list
    Then <addsupervisor approve> completed

  Scenario: Edit New Supervisor
    Given login to ims
    And <organization registry supList> load page
    And check page loaded < Баталгаажуулах албан тушаалтан жагсаалт >
    When <edit> supervisor to list
    Then <edit supervisor> completed

  Scenario: Delete New Supervisor
    Given login to ims
    And <organization registry supList> load page
    And check page loaded < Баталгаажуулах албан тушаалтан жагсаалт >
    When <delete> supervisor to list
    Then <delete selectedsupervisor> completed