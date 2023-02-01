Feature: mik-system-XML
    Scenario: add information in mik-system-xml menu
        Given login to ims
            And <mik-xml> load page
            And check page loaded <ӨӨРЧЛӨЛТИЙН МЭДЭЭЛЭЛ>
        When mik-system-xml add information
        Then <mikSystem xml add-information> completed

    Scenario: Inquiry positive
        Given login to ims
            And <mik-xml> load page
            And check page loaded <ӨӨРЧЛӨЛТИЙН МЭДЭЭЛЭЛ>
        When insert date time and press inquire button
        Then data will be shown

    Scenario: Download excel file Positive
        Given login to ims
        And <mik-xml> load page
        And check page loaded <ӨӨРЧЛӨЛТИЙН МЭДЭЭЛЭЛ>
        When click on download excel button