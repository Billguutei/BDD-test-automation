Feature: гэрээ шинэчлэх

    Scenario Outline: <scenario_any>
    Given Enter <var_> and <col_name> and contract and customer-service
    When Connect to server contract and POST
    Then Result <response>

    @branch
    Examples: check "branch"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|branch|
    |Урт шалгах|1|1000|branch|
    |formatting error|2|1000|branch|

    @cif
    Examples: check "cif"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|cif|
    |Урт шалгах|1|1000|cif|
    |formatting error|2|1000|cif|
    |Enter a correct value|3|1002|cif|

    @domainId
    Examples: check "domainId"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|domainId|
    |Урт шалгах|1|1000|domainId|
    |formatting error|2|1000|domainId|