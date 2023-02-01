Feature: cif - г идэвхтэй,идэвхгүй гэх мэт төсөв өөрчиллөх
    Scenario Outline: <scenario_any>
    Given Enter <var_> and <col_name> and activate and customer-service
    When Connect to server activate and PUT
    Then Result <response>

    @branch
    Examples: check "branch"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|branch|
    |Урт шалгах|1|1000|branch|
    |formatting error|2|1000|branch|    

    @teller
    Examples: check "teller"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|teller|
    |Урт шалгах|1|1000|teller|
    |formatting error|2|1000|teller|    

    @terminal
    Examples: check "terminal"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|terminal|
    |Урт шалгах|1|1000|terminal|
    |formatting error|2|1000|terminal|    

    @cif
    Examples: check "cif"
    |scenario_any|var_|response|col_name|
    |Хоосон байхад|0|1000|cif|
    |Урт шалгах|1|1000|cif|
    |formatting error|2|1000|cif|    