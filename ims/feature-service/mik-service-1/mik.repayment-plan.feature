Feature: Repayment plan menu in ims-mik_systems

 Scenario: Download excel file positive
   Given login to ims
   And <mik-repayment plan> load page
   And check page loaded <Эргэн төлөлт харах>
   Then mik-repayment-plan <download excel>

 Scenario: Download example file positive
   Given login to ims
   And <mik-repayment plan> load page
   And check page loaded <Эргэн төлөлт харах>
   When mik-repayment-plan <download example excel>
   Then <mik example-repayment-plan> file will be downloaded
 Scenario: Inquire repayment calculation plan Positive
   Given login to ims
   And <mik-repayment plan> load page
   And check page loaded <Эргэн төлөлт харах>
   Then mik-repayment-plan <inquire repayment>

 Scenario: Inquire repayment create xml
    Given login to ims
    And <mik-repayment plan> load page
    And check page loaded <Эргэн төлөлт харах>
    Then mik-repayment-plan <create xml>
     
 Scenario: Calculate a repayment plan Positive
   Given login to ims
   And <mik-repayment plan> load page
   And check page loaded <Эргэн төлөлт харах>
   When mik-repayment-plan <calculate repayment plan>
   Then <mikSystem repaymentPlan calculation> complete

  