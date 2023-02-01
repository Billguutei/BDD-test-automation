Feature: Group Operations

 Scenario: Add Group
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Данс нээх >
   And etc document <Бүлэг нэмэх> <Данс нээх >
   When <add group> in document service
   Then <edit-document add-group> completed

 Scenario: Edit Group
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Данс нээх >
   And etc document <Бүлэг засах> <Данс нээх >
   When <edit group> in document service
   Then <edit-document edit-group> completed

 Scenario: Add Document to group
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <testing>
   And etc document <Док нэмэх> <testing>
   When <add document> in document service
   Then <edit-document add-document> completed

  Scenario: Edit Document from group
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <testing123 >
   And etc document <Док засах> <testing123 >
   When <edit document> in document service
   Then <edit-document edit-document> completed

 Scenario: Delete Document from group
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <testing123 >
   And etc document <Док устгах> <testing123 >
   When <delete document> in document service
  #  Then check if document is deleted

  Scenario: Delete Group
    Given login to ims
    And <document-maintenance> load page
    And check page loaded <testing>
    And etc document <Бүлэг устгах> <testing>
    When <delete group> in document service
    Then check if group is deleted