Feature: User access menu IMS

  Scenario: Edit user access in User Access Menu Positive
    Given login to ims
      And <access-user access> load page
      And check page loaded <Салбар-аар Ажилтан шүүх:>
    When <edit> user access
    Then <update user> completed

  # Scenario: Inquire user access in User Access Menu Positive
  #   Given login to ims
  #     And <access-user access> load page
  #     And check page loaded <Салбар-аар Ажилтан шүүх:>
  #   When <inquire access> user access

  Scenario: Add user access in User Access Menu Positive
    Given login to ims
      And <access-user access> load page
      And check page loaded <Салбар-аар Ажилтан шүүх:>
    When <add access> user access
    Then <add user> completed

  Scenario: Delete user access in User Access Menu Positive
    Given login to ims
      And <access-user access> load page
      And check page loaded <Салбар-аар Ажилтан шүүх:>
    When <delete access> user access
    Then <delete user> completed

  # Scenario: Change status of an employee in User Access Menu Positive
  #   Given login to ims
  #     And <access-user access> load page
  #     And check page loaded <Салбар-аар Ажилтан шүүх:>
  #   When <change status> user access
  #   Then <identityService userAccess changeStatus> completed

