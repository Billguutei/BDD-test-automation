Feature: Download updated contract report

    Scenario: Insert startendDate and click download button
       Given login to ims
           And <report_contract> load page
           And check page loaded <Гэрээ шинэчилсэн тайлан татах>
       Then matching date and download