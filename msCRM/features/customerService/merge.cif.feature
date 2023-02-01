Feature: Буруу cif - г идэвхгүй болгоод зөв cif - руу данс -г нь зөөх
    Scenario Outline: <scenario_any>
    Given Enter <var_> and <col_name> and mergecif and customer-service
    When Connect to server mergecif and POST
    Then Result <response>

    @branch
    Examples: check "branch"
    |scenario_any|var_|response|col_name|
    |салбар дугаар оруулах|0|1000|branch|
    |хоосон утгаар шалгах|1|1000|branch|
    |Урт  шалгах|2|1000|branch|  
    |teller дугаар оруулж үзэх|3|1000|branch| 

    @teller
    Examples: check "teller"
    |scenario_any|var_|response|col_name|
    |teller-н дугаар оруулах|0|1000|teller|
    |форматын алдаатай, байхгүй дугаараар шалгах|1|1000|teller|

    @terminal
    Examples: check "terminal"
    |scenario_any|var_|response|col_name|
    |Формат шалгах|0|1000|terminal|
    |Урт шалгах|1|1000|terminal|
    |String|2|1000|terminal| 
    |Буруу утга оруулах|3|1000|terminal| 
    |хоосон|4|1000|terminal|
    |TerNumber|5|1000|terminal|

    @incorrect_cif
    Examples: check "inCorrectCif"
    |scenario_any|var_|response|col_name|
    |Формат шалгах|0|1000|inCorrectCif|
    |Урт шалгах|1|1000|inCorrectCif|
    |String|2|1000|inCorrectCif| 
    |Буруу утга оруулах|3|1000|inCorrectCif| 
    |хоосон|4|1000|inCorrectCif|
    |Данс оруулж үзэх|5|1000|inCorrectCif|


    @correct_cif
    Examples: check "correctCif"
    |scenario_any|var_|response|col_name|
    |форматын алдаатай|0|1000|correctCif|
    |хоосон утгаар шалгах|1|1000|correctCif|

    #|incorrectCif - тай ижил cif оруулах|0|1000|correctCif|
    #|cif merge хийж үзэх|0|1000|correctCif|




    