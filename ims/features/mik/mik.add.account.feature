Feature: Add Account menu in ims-mik systems
 Scenario: Delete account positive
   Given login to ims
   And <mik-add account> load page
   And check page loaded <ӨӨРЧЛӨЛТИЙН МЭДЭЭЛЭЛ>
   When mik-add-account <inquire account>
   And mik-add-account <delete account>
   Then <mikSystem addAccount deleteAccount> completed

 Scenario: Inquire Account Positive
   Given login to ims
   And <mik-add account> load page
   And check page loaded <ӨӨРЧЛӨЛТИЙН МЭДЭЭЛЭЛ>
   When mik-add-account <inquire account>
   Then mik-add-account <delete account>

  Scenario: Download excel file Positve
    Given login to ims
    And <mik-add account> load page
    And check page loaded <ӨӨРЧЛӨЛТИЙН МЭДЭЭЛЭЛ>
    When mik-add-account <inquire account>
    Then mik-add-account <download excel>
