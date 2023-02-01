Feature: Онлайн бүртгэл үйлчилгээ 


 Scenario: Add Source to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <add source> in document service
   Then <edit-document add-source> completed

 Scenario: Delete Source to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <delete source> in document service
   Then <edit-document delete-source> completed

 Scenario: Add Field to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <add field> in document service
   Then <edit-document add-field> completed

 Scenario: Edit Field to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <edit field> in document service
   Then <edit-document edit-field> completed

 Scenario: Delete Field to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <delete field> in document service
   Then <edit-document delete-field> completed

#  Scenario: Change Order to document Menu Positive .Онлайн бүртгэл үйлчилгээ
#    Given login to ims
#    And <document-maintenance> load page
#    And check page loaded <.Онлайн бүртгэл үйлчилгээ >
#    And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
#    And check page loaded < Бичиг баримтын сурвалжууд >
#    When <change order> in document service
#    Then <edit-document change-order> completed

 Scenario: Document Inputs to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <document inputs empty> in document service

 Scenario: Edit HTML to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <edit-html> in document service
   Then <edit-document edit-html> completed

 Scenario: Add Related Form to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <add-related-form> in document service
   Then <edit-document add-related-form> completed

 Scenario: Change Configs to document Menu Positive .Онлайн бүртгэл үйлчилгээ
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <.Онлайн бүртгэл үйлчилгээ >
   And etc document <HTML засах> <.Онлайн бүртгэл үйлчилгээ >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <change-configs> in document service
   Then <edit-document change-configs> completed

Scenario: Add Source to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <add source> in document service
   Then <edit-document add-source> completed

 Scenario: Delete Source to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <delete source> in document service
   Then <edit-document delete-source> completed

 Scenario: Add Field to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <add field> in document service
   Then <edit-document add-field> completed

 Scenario: Edit Field to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <edit field> in document service
   Then <edit-document edit-field> completed

 Scenario: Delete Field to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <delete field> in document service
   Then <edit-document delete-field> completed

#  Scenario: Change Order to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
#    Given login to ims
#    And <document-maintenance> load page
#    And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
#    And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
#    And check page loaded < Бичиг баримтын сурвалжууд >
#    When <change order> in document service
#    Then <edit-document change-order> completed

 Scenario: Document Inputs to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <document inputs empty> in document service

 Scenario: Edit HTML to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <edit-html> in document service
   Then <edit-document edit-html> completed

 Scenario: Add Related Form to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <add-related-form> in document service
   Then <edit-document add-related-form> completed

 Scenario: Change Configs to document Menu Positive .Онлайн бүртгэл үйлчилгээ - 1
   Given login to ims
   And <document-maintenance> load page
   And check page loaded <Баталгаат гарын үсэг шинэчлэх  >
   And etc document <HTML засах> <Баталгаат гарын үсэг шинэчлэх  >
   And check page loaded < Бичиг баримтын сурвалжууд >
   When <change-configs> in document service
   Then <edit-document change-configs> completed