Feature: Inquire tax report
  Scenario:  Tax type Invoice number
    Given login to ims
        And <tax_window> load page
        And check page loaded <Тайлан лавлах>
    When <invoice_number> fill date and search
    #Then <invoice_number_result> take screenshot succesfull

  Scenario:  Tax type Үл хөдлөх эд хөрөнгө ҮХЭХ-ийн улсын бүртгэлийн гэрчилгээний дугаар 
    Given login to ims
        And <tax_window> load page
        And check page loaded <Тайлан лавлах>
    When <state_registration_certificate_number> fill date and search

  Scenario:  Tax type Тээврийн хэрэгслийн арлын дугаар  
    Given login to ims
        And <tax_window> load page
        And check page loaded <Тайлан лавлах>
    When <vehicle_number> fill date and search

  Scenario:  Tax type Тээврийн хэрэгслийн улсын бүртгэлийн дугаар 
    Given login to ims
        And <tax_window> load page
        And check page loaded <Тайлан лавлах>
    When <vehicle_state_registration_number> fill date and search

  Scenario:  Tax type Галт зэвсгийн гол төмрийн дугаар 
    Given login to ims
        And <tax_window> load page
        And check page loaded <Тайлан лавлах>
    When <main_iron_number_of_the_firearm> fill date and search

  Scenario:  Tax type Галт зэвсгийн гэрчилгээний дугаар 
    Given login to ims
        And <tax_window> load page
        And check page loaded <Тайлан лавлах>
    When <firearms_certificate_number> fill date and search