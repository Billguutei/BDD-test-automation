Feature: hide

    Scenario Outline: <scenario_any>
    Given Enter <var_> and <col_name> and hide and customer-service
    When Connect to server hide and POST
    Then Result <response>

    @account_and_cif
    Examples: check "cifAccountNumber"
    |scenario_any|var_|response|col_name|
    |formatting error|0|1000|cifAccountNumber|
    |хаагдсан данс лавлах|1|1001|cifAccountNumber|
    |status Closed дансны дугаар оруулах|2|1002|cifAccountNumber|
    |онлайн хугацаатай хадгаламж|3|1003|cifAccountNumber|
    |байгууллагын тусгай|4|1003|cifAccountNumber|
    |хүүгээс хүү бодох|5|1003|cifAccountNumber|
    |онлайн зээл|6|1003|cifAccountNumber|
    |депозит данс лавлах|7|1003|cifAccountNumber|
    |зээлийн данс лавлах|8|1003|cifAccountNumber|
    |cif оруулахад|9|1003|cifAccountNumber|
    |Хоосон байхад|10|1003|cifAccountNumber|


    @branch
    Examples: check "branch"
    |scenario_any|var_|response|col_name|
    |салбар дугаар оруулах|0|1000|branch|
    |хоосон утгаар шалгах|1|1001|branch|
    |уртын хэмжээн мах утга оруулах|2|1001|branch|
    |салбар дугаараар шалгах|3|1001|branch|
    |буруу салбар оруулах|4|1001|branch|


    @teller
    Examples: check "cifAccountNumber"
    |scenario_any|var_|response|col_name|
    |teller-н дугаар оруулах|0|1000|teller|
    |форматын алдаатай|1|1000|teller|
    |талбарыг хоосон шалгах|2|1000|teller|

    @terminal
    Examples: check "cifAccountNumber"
    |scenario_any|var_|response|col_name|
    |формат шалгах|0|1000|terminal|
    |Урт  шалгах|1|1001|terminal|
    |string|2|1001|terminal|
    |Буруу утга оруулах|2|1001|terminal|
    |хоосон утга оруулах|2|1001|terminal|

    @system
    Examples: check "cifAccountNumber"
    |scenario_any|var_|response|col_name|
    |формат шалгах|0|1000|cifAccountNumber|
    |Урт шалгах|1|1001|cifAccountNumber|
    |int|2|1001|cifAccountNumber|
    |Буруу утга оруулах|2|1001|cifAccountNumber|
    |хоосон утга оруулах|2|1001|cifAccountNumber|
    |sysNumber|2|1001|cifAccountNumber|
    |данс оруулаад CIF төрлөөр шалгаж үзэхэд|2|1001|cifAccountNumber|

    @security_code_level
    Examples: check "securityCodeLevel"
    |scenario_any|var_|response|col_name|
    |формат шалгах|0|1000|securityCodeLevel|
    |Урт шалгах|1|1001|securityCodeLevel|
    |string|2|1001|securityCodeLevel|
    |Буруу утга оруулах|3|1001|securityCodeLevel|
    |хоосон утга оруулах|4|1001|securityCodeLevel|
    |secNumber|5|1001|securityCodeLevel|

    @user_to_access
    Examples: check "cifAccountNumber"
    |scenario_any|var_|response|col_name|
    |формат шалгах|0|1000|userToAccess|
    |Урт шалгах|1|1001|userToAccess|
    |string|2|1001|userToAccess|
    |Буруу утга оруулах|3|1001|userToAccess|
    |хоосон утга оруулах|4|1001|userToAccess|
    |AcessNumber|5|1001|userToAccess|

    @branch_to_access
    Examples: check "branchToAccess"
    |scenario_any|var_|response|col_name|
    |формат шалгах|0|1000|branchToAccess|
    |Урт шалгах|1|1001|branchToAccess|
    |string|2|1001|branchToAccess|
    |Буруу утга оруулах|3|1001|branchToAccess|
    |хоосон утга оруулах|4|1001|branchToAccess|