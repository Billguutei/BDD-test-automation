Feature: Update customer information

    Scenario Outline: <scenario_any>
    Given Enter <var_> and <col_name> and setCustomer and customer-service
    When Connect to server setCustomer and PUT
    Then Result <response>

    @cif
    Examples: check cif
    |scenario_any|var_|response|col_name|
    |corret cif|0|1000|cif|
    |formatting error|1|1001|cif|
    |check for empty value|2|1002|cif|
    |check for inactive cif|3|1003|cif|
    
    @vip
    Examples: check vip
    |scenario_any|var_|response|col_name|
    |Normal|0|1000|vipcode|
    |Priority|1|1000|vipcode|
    |signature|2|1000|vipcode|
    |Corp|3|1000|vipcode|
    |Mass|4|1000|vipcode|
    |SME|5|1000|vipcode|
    |Төрийн байгууллага|6|1000|vipcode|
    |Санхүүгийн байгууллага|7|1000|vipcode|

    # @customer_type
    # Examples: check customer_type
    # |scenario_any|var_|response|col_name|
    # |Mongolian citizen|0|1000|custType|
    # |State organization account|1|1000|custType|
    # |Private corporate account|2|1000|custType|
    # |Government account|3|1000|custType|
    # |Domestic BSB account|4|1000|custType|
    # |Гадаадын  ЭЗ - н харъяат  бус байгууллага|5|1000|custType|
    # |Өрх гэр , иргэнд  үйлчлэгч  УТ/нам|6|1000|custType|

    # @title_code
    # Examples: check titleCode
    # |scenario_any|var_|response|col_name|
    # |corret titleCode|0|1000|titleCode|

    # @business_name
    # Examples: check businessName
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|businessName|
    # |Enter a empty value|1|1000|businessName|
    # |Long check|2|1000|businessName|

    # @address1
    # Examples: check address1
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|addr1|
    # |Enter a empty value|1|1000|addr1|

    # @post_code
    # Examples: check postCode
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|postCode|

    # @nationality 
    # Examples: check nationality
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|nationality|
    # |Long check|1|1000|nationality|
    # |Enter a empty value|2|1000|nationality|
    # |Enter a number value|3|1000|nationality|

    # @domicile1
    # Examples: check domicile1
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|domicile1|
    # |Long check|1|1000|domicile1|
    # |Enter a value that does not exist|2|1000|domicile1|

    # @passport_country
    # Examples: check passport_country
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|passportCountry|
    # |Long check|1|1000|passportCountry|

    # @home_phone_num
    # Examples: check home_phone_num
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|homePhoneNum|
    # |Long check|1|1000|homePhoneNum|

    # @occupancy_code
    # Examples: check occupancy_code
    # |scenario_any|var_|response|col_name|
    # |H|0|1000|occupancyCode|
    # |T|1|1000|occupancyCode|
    # |F|2|1000|occupancyCode|
    # |O|3|1000|occupancyCode|

    # @fax_num
    # Examples: check fax_num
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|faxNum|

    # @lang_code
    # Examples: check lang_code
    # |scenario_any|var_|response|col_name|
    # |Mongolia|0|1000|langCode|
    # |Russia|1|1000|langCode|
    # |English|2|1000|langCode|
    # |Long check|3|1000|langCode|

    # @mobile_num
    # Examples: check mobile_num
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|mobileNum|
    # |Long check|1|1000|mobileNum|

    # @business_phone_num
    # Examples: check business_phone_num
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|businessPhoneNum|
    # |Enter a empty value|1|1000|businessPhoneNum|

    # @addr3
    # Examples: check addr3
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|addr3|

    # @addr4
    # Examples: check addr4
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|addr4|

    # @segment_code
    # Examples: check segment_code
    # |scenario_any|var_|response|col_name|
    # |Монол банк|0|1000|segmentCode|
    # |Даатгалын компани|1|1000|segmentCode|
    # |Үнэт цасны компани|2|1000|segmentCode|
    # |Банк бус санхүү-н байгуулга|3|1000|segmentCode|
    # |Хадгаламж зээл-н хоршоо|4|1000|segmentCode|
    # |Хөгжилийн банк|5|1000|segmentCode|
    # |Санхүүгийн байг-бусад|6|1000|segmentCode|
    # |ЭЗХАХБГиш орны банк|7|1000|segmentCode|
    # |ЭЗХАХБГиш бус оны БС|8|1000|segmentCode|
    # |ОС Бус гад-н улсын байгуулга|9|1000|segmentCode|
    # |ОС Бус гад-н хувийн сек|10|1000|segmentCode|
    # |ЭЗ харьяат бус-бусад|11|1000|segmentCode|
    # |Ашгийн бус байгуулга|12|1000|segmentCode|
    # |Монгол иргэд|13|1000|segmentCode|
    # |Төрийн өмчит ААТҮГ|14|1000|segmentCode|
    # |Орон нут/өмчит  ААТҮГ|15|1000|segmentCode|
    # |Төрийн өмчит ХК|16|1000|segmentCode|
    # |Т/Ө ХХК|17|1000|segmentCode|
    # |О/н өмчит ХХК|18|1000|segmentCode|
    # |ОС гад-ны улсын байгуулга|19|1000|segmentCode|
    # |Хувийн байг/ХК|20|1000|segmentCode|
    # |Хувийн байг/ Нөхөрлөл|21|1000|segmentCode|
    # |Хувийн байг/Бусад|22|1000|segmentCode|
    # |Хувийн байг /ХХК|23|1000|segmentCode|
    # |ОС гадаадын хувийн сек|24|1000|segmentCode|
    # |Эдгээрээс бусад утга|25|1000|segmentCode|
    # |харилцагчийн төрөл оруулах|26|1000|segmentCode|

    # @locker_holder
    # Examples: check locker_holder
    # |scenario_any|var_|response|col_name|
    # |Yes|0|1000|lockerHolder|
    # |No|1|1000|lockerHolder|
    # |Long check|2|1000|lockerHolder|
    
    # @branch
    # Examples: check branch
    # |scenario_any|var_|response|col_name|
    # |Treasury Branch|0|1000|branch|
    # |Pitt Street Branch|1|1000|branch|
    # |George Street Branch|2|1000|branch|
    # |Head Office Branch|3|1000|branch|
    # |Салбар оруулахад|4|1000|branch|
    # |Хоосон утга оруулах|5|1000|branch|

    # @bor_risk1
    # Examples: check bor_risk1
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|bor_risk1|

    # @bor_risk_dt1
    # Examples: check bor_risk_dt1
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|bor_risk_dt1|
    
    # @register
    # Examples: "check Регистр №"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|idNum|
    # |Enter only digit value|1|1000|idNum|
    # |Enter empty value|2|1000|idNum|
    # |Long check|3|1000|idNum|
    # |Enter an existing value|4|1000|idNum|
     
    # @id_issue_dt 
    # Examples: check "ID олгосон Огноо"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|idIssueDt|
    # |Enter a incorrect value|1|1000|idIssueDt|
    # |Long check|2|1000|idIssueDt|

    # @id_issue_place
    # Examples: check "хаана Олгосон"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|idIssuePlace|

    # @email
    # Examples: check "Е-мэйл"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|email|
    # |formatting error|1|1000|email|
    # |Enter empty value|2|1000|email|

    # @cust_limit_ind
    # Examples: check "customer limit"
    # |scenario_any|var_|response|col_name|
    # |Yes|0|1000|custLimitInd|
    # |Long check|1|1000|custLimitInd|
    # |No|2|1000|custLimitInd|

    # @influential_political_person
    # Examples: check "улс төрд нөлөө бүхий этгээд "
    # |scenario_any|var_|response|col_name|
    # |Yes|0|1000|influentialPoliticalPerson|
    # |No|1|1000|influentialPoliticalPerson|
    # |Long check|2|1000|influentialPoliticalPerson|

    # @relationship_manager_num
    # Examples: check "Хариуцсан ажилтан"
    # |scenario_any|var_|response|col_name|
    # |Long check|0|1000|relationshipManagerNum|
    # |Enter a string value|1|1000|relationshipManagerNum|
    # |Enter a correct value|2|1000|relationshipManagerNum|

    # @tax_payer_number
    # Examples: check "Татвар төлөгчийн дугаар"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|taxPayerNumber|
    # |Long check|1|1000|taxPayerNumber|
    # |Enter a correct value|2|1000|taxPayerNumber|

    # @registered_business_num
    # Examples: check "Үйл ажиллагааны чиглэл"
    # |scenario_any|var_|response|col_name|
    # |Enter a another value|0|1000|registeredBusinessNum|
    # |Long check |1|1000|registeredBusinessNum|
    # |Банк|2|1000|registeredBusinessNum|
    # |Ломбард|3|1000|registeredBusinessNum|

    # @contact_title_code1
    # Examples: check "Цол Хэргэм"
    # |scenario_any|var_|response|col_name|
    # |Enter a corret value (Ноён)|0|1000|contactTitleCode1|
    # |Long check|1|1000|contactTitleCode1|
    # |Enter a empty value|2|1000|contactTitleCode1|

    # @contact_name1_1
    # Examples: check "Овог 1"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|contactName1_1|
    # |Enter a empty value|1|1000|contactName1_1|
    # |Long check|2|1000|contactName1_1|

    # @contact_name1_2
    # Examples: check "Нэр 1"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|contactName1_2|
    # |Enter a empty value|1|1000|contactName1_2|
    # |Long check|2|1000|contactName1_2|

    # @contact_name1_3
    # Examples: check "Регистр1"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|contactName1_3|
    # |Enter a empty value|1|1000|contactName1_3|
    # |Long check|2|1000|contactName1_3|

    # @contact_fax_num1
    # Examples: check "Паспорт No"
    # |scenario_any|var_|response|col_name|
    # |Enter a number value|0|1000|contactFaxNum1|
    # |Enter a empty value|1|1000|contactFaxNum1|
    # |Enter a string value|2|1000|contactFaxNum1|
    # |Long check|3|1000|contactFaxNum1|
    
    #     #Байгууллага дэлгэрэнгүй
    # @second_business_add_loc_line2_3
    # Examples: check "Иргэншил"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|secondBusinessAddLocLine2_3|
    # |Long check|1|1000|secondBusinessAddLocLine2_3|
    # |Enter a empty value|2|1000|secondBusinessAddLocLine2_3|
    # |Enter a number value|3|1000|secondBusinessAddLocLine2_3|

    #     #Байгууллага дэлгэрэнгүй
    # @second_business_addLoc_line4_2
    # Examples: check "Огноо"
    # |scenario_any|var_|response|col_name|
    # |Enter a correct value|0|1000|secondBusinessAddLocLine4_2|
    # |Enter a string value|1|1000|secondBusinessAddLocLine4_2|
    # |Long check|2|1000|secondBusinessAddLocLine4_2|
    # |Enter a empty value|3|1000|secondBusinessAddLocLine4_2|
    # |Enter a formatted error value|4|1000|secondBusinessAddLocLine4_2|

    #     #Байгууллага дэлгэрэнгүй
    # @second_business_add_loc_line3_2
    # Examples: check "Албан Тушаал"
    # |scenario_any|var_|response|col_name|
    # |Enter a number value|0|1000|secondBusinessAddLocLine3_2|
    # |Enter a string value|1|1000|secondBusinessAddLocLine3_2|
    # |Long check|2|1000|secondBusinessAddLocLine3_2|
    # |Enter a empty value|3|1000|secondBusinessAddLocLine3_2|

    #     #Байгууллага дэлгэрэнгүй
    # @contact_phone_num1
    # Examples: check "Гар Утас"
    # |scenario_any|var_|response|col_name|
    # |Enter a number value|0|1000|contactPhoneNum1|
    # |Enter a string value|1|1000|contactPhoneNum1|
    # |Long check|2|1000|contactPhoneNum1|
    # |Enter a empty value|3|1000|contactPhoneNum1|

    #         #Байгууллага дэлгэрэнгүй
    # @gazette_num
    # Examples: check "Худалдаа Лицензийн №"
    # |scenario_any|var_|response|col_name|
    # |Enter a number value|0|1000|gazetteNum|
    # |Enter a string value|1|1000|gazetteNum|
    # |Long check|2|1000|gazetteNum|
    # |Enter a empty value|3|1000|gazetteNum|
    

    #         #Байгууллага дэлгэрэнгүй
    # @name1
    # Examples: check "Бүтэн/нэр"
    # |scenario_any|var_|response|col_name|
    # |Enter a number value|0|1000|name1|
    # |Enter a string value|1|1000|name1|
    # |Long check|2|1000|name1|
    # |Enter a empty value|3|1000|name1|

    #         #Байгууллага дэлгэрэнгүй
    # @nationaity1
    # Examples: check "Иргэншил"
    # |scenario_any|var_|response|col_name|
    # |Enter a number value|0|1000|nationaity1|
    # |Enter a string value|1|1000|nationaity1|
    # |Long check|2|1000|nationaity1|
    # |Enter a empty value|3|1000|nationaity1|

    #         #Байгууллага дэлгэрэнгүй
    # @registration_number1
    # Examples: check "РД"
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|1|1000|registrationNumber1|
    # |Long check|2|1000|registrationNumber1|
    # |Enter a empty value|3|1000|registrationNumber1|

    # # @test1
    # # Scenario: test 1
    # # Given test signature

    # #Retail 
    # Scenario Outline: <scenario_retail>
    # Given Enter1 <var_> and <col_name> and setCustomer and setcustomer-retail
    # When Connect to server setCustomer and PUT
    # Then Result <response>

    # @lastname
    # Examples: check lastname
    # |scenario_customer_type|var_|response|col_name|
    # |Enter a string value|0|1000|custFirstName|
    # |Long a check|1|1000|custFirstName|
    # |Enter a empty value|2|1000|custFirstName|

    # @firstname
    # Examples: check firstname
    # |scenario_customer_type|var_|response|col_name|
    # |Enter a string value|0|1000|custLastName|
    # |Long a check|1|1000|custLastName|
    # |Enter a empty value|2|1000|custLastName|

    # # N,E,S,R,H,T,C
    # @employment
    # Examples: check "Ажил эрхлэлт  - Х/төрөл 50,60,70 хамаарна"
    # |scenario_retail|var_|response|col_name|
    # |Enter a "N" value|0|1000|employment|
    # |Enter a "E" value|1|1000|employment|
    # |Enter a "S" value|2|1000|employment|
    # |Enter a "R" value|3|1000|employment|
    # |Enter a "H" value|4|1000|employment|
    # |Enter a "T" value|5|1000|employment|
    # |Enter a "C" value|6|1000|employment|
    # |Long check|7|1000|employment|

    # @gender_1
    # Examples: check "Хүйс"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|gender_1|
    # |Long check|1|1000|gender_1|

    # @id_issue_place
    # Examples: check "Гэр бүлийн байдал"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|idIssuePlace|

    # @religion
    # Examples: check "Шашин"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|religion|
    # |Enter a correct value|1|1000|religion|
    # |Long check|2|1000|religion|

    # @lastnameLatin
    # Examples: check lastnameLatin
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|contractName1_1|
    # |Long check|1|1000|contractName1_1|

    # @firstnameLatin
    # Examples: check lastnameLatin
    # |scenario_any|var_|response|col_name|
    # |Enter a string value|0|1000|contractName1_2|
    # |Long check|1|1000|contractName1_2|

    # @birth_place
    # Examples: check "Төрсөн газар"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|birthPlace|

    # @currEmpName
    # Examples: check "АжлынГазарНэр"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|currEmpName|

    # @postOfficeBox
    # Examples: check "Шуудангийн хайрцаг"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|postOfficeBox|

    # @city_1
    # Examples: check "Хот"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|city_1|

    # @emplyedSince2
    # Examples: check "Ажилд орсон огноо"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|emplyedSince2|

    # @currEmpAddr1
    # Examples: check "Хаяг 1"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|currEmpAddr1|

    # @
    # Examples: check "Боловсрол"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000||
    # |Enter a string value|0|1000||

    # @currEmpAddr2
    # Examples: check "Хаяг 2"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|currEmpAddr2|

    # @
    # Examples: check "Емэйл хаяг"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000||

    # @occupationDesc1
    # Examples: check "Албан тушаал"
    # |scenario_retail|var_|response|col_name|
    # |1-65 өөр үр дүн оруулж үзэх|0|1000|occupationDesc1|
    # |1-65 хүртэл сонголт|1|1000|occupationDesc1|

    # @bussDesc
    # Examples: check "Бизнесийн тодорхойлолт"
    # |scenario_retail|var_|response|col_name|
    # |Enter a string value|0|1000|bussDesc|

    # /////////////////////////////////////////////////////////////////////////////////
    
    # Салбарын ангилал өөрчилөлт хийж байгаа бол салбарын дэд ангилал 
    # бас өөрчилөгдөх ёстой.
    
    # @indcode2
    # Examples: check indcode2
    # |scenario_retail|var_|response|col_name|
    # |A|0|1000|indcode2|
    # |B|1|1000|indcode2|
    # |C|2|1000|indcode2|
    # |D|3|1000|indcode2|
    # |E|4|1000|indcode2|
    # |F|5|1000|indcode2|
    # |G|6|1000|indcode2|
    # |H|7|1000|indcode2|
    # |I|8|1000|indcode2|
    # |J|9|1000|indcode2|
    # |K|10|1000|indcode2|
    # |L|11|1000|indcode2|
    # |M|12|1000|indcode2|
    # |O|13|1000|indcode2|
    # |P|14|1000|indcode2|
    # |Q|15|1000|indcode2|
    # |R|16|1000|indcode2|
    # |S|17|1000|indcode2|
    # |T|18|1000|indcode2|
    # |U|19|1000|indcode2|
    # |X|20|1000|indcode2|
    # |Y|21|1000|indcode2|
    # |Z|22|1000|indcode2|

    # @indsubcode2
    # Examples: check indcode2
    # |scenario_retail|parent_|var_|response|col_name|
    # |A|1101|0|1000|indsubcode2|
    # |B|5100|1|1000|indsubcode2|
    # |C|10100|2|1000|indsubcode2|
    # |D|35101|3|1000|indsubcode2|
    # |E|36000|4|1000|indsubcode2|
    # |F|41000|5|1000|indsubcode2|
    # |G|45100|6|1000|indsubcode2|
    # |H|49200|7|1000|indsubcode2|
    # |I|55000|8|1000|indsubcode2|
    # |J|58000|9|1000|indsubcode2|
    # |K|64000|10|1000|indsubcode2|
    # |L|65000|11|1000|indsubcode2|
    # |M|70000|12|1000|indsubcode2|
    # |O|84100|13|1000|indsubcode2|
    # |P|85100|14|1000|indsubcode2|
    # |Q|86000|15|1000|indsubcode2|
    # |R|94000|16|1000|indsubcode2|
    # |S|97000|17|1000|indsubcode2|
    # |T|99000|18|1000|indsubcode2|
    # |U|19100|19|1000|indsubcode2|
    # |X|32900|20|1000|indsubcode2|
    # |Y|33200|21|1000|indsubcode2|
    # |Z|24100|22|1000|indsubcode2|











