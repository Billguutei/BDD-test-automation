Feature: Account definition Deduction report

    Scenario: Insert fullDate and click download button
       Given login to ims
           And <report> load page
           And check page loaded <Дансны тодорхойлолт- Хураамж суутгасан тайлан>
       Then matching date and download