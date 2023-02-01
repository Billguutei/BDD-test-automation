Feature: vip код-г солих

    Scenario Outline: <scenario_any>
    Given Enter <var_> and <col_name> and segment and customer-service
    When Connect to server segment and POST
    Then Result <response>

    @branch
    Examples: check "branch"
    |scenario_any|var_|response|col_name|
    |Хоосон утга оруулах|0|1000|branch|
    |Урт шалгах|1|1001|branch|
    |формат шалгах|2|1002|branch|

    @teller
    Examples: check "teller"
    |scenario_any|var_|response|col_name|
    |Хоосон утга оруулах|0|1000|teller|
    |Урт шалгах|1|1001|teller|

    @terminal
    Examples: check "terminal"
    |scenario_any|var_|response|col_name|
    |Хоосон утга оруулах|0|1000|terminal|
    |Урт шалгах|1|1001|terminal|
    |формат шалгах|2|1002|terminal|

    @cif
    Examples: check "cif"
    |scenario_any|var_|response|col_name|
    |Хоосон утга оруулах|0|1000|cif|
    |Урт шалгах|1|1001|cif|
    |формат шалгах|2|1002|cif|

    @segmentCode
    Examples: check "segmentCode"
    |scenario_any|var_|response|col_name|
    |Хоосон утга оруулах|0|1000|segmentCode|
    |Урт шалгах|1|1001|segmentCode|
    |string оруулах|2|1001|segmentCode|
    |өөрчилөлт оруулж үзэх|3|1001|segmentCode|