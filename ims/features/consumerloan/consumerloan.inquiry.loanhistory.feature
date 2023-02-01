Feature: inquiry loan history
    Scenario: inquiry loan history search by cif positive
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <cif>
    Then <page-content> screen shot by class name <inquiry_loan_history_by_cif_positive>

    Scenario: inquiry loan history search by register positive
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <register_no>
    Then <page-content> screen shot by class name <inquiry_loan_history_by_register_positive>

    Scenario: inquiry loan history search by null cif or register
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <null>
    Then <null cif loanhistory> completed
    Then <page-content> screen shot by class name <inquiry_loan_history_by_null_cif_negative>

    Scenario: inquiry loan history search by wrong cif or register
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <wrongvalue1>
    Then <string value> completed
    Then <page-content> screen shot by class name <inquiry_loan_history_stringvalue_negative>

    Scenario: inquiry loan history search by wrong cif or register
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <wrongvalue2>
    Then <number value> completed
    Then <page-content> screen shot by class name <inquiry_loan_history_numbervalue_negative>

    Scenario: inquiry loan history search by empty register
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <emptyregister>
    Then <empty register> completed
    Then <page-content> screen shot by class name <inquiry_loan_history_empty_register_negative>

    Scenario: inquiry loan history search by cif without check digit
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <nocheckdigit>
    Then <no checkdigit cif> completed
    Then <page-content> screen shot by class name <inquiry_loan_history_no_checkdigitcif_negative>

    Scenario: inquiry loan history search by cif no customer
        When login to ims
            And <inquiry_loan_history_consumerloan> load page
            And check page loaded < Зээлийн түүх лавлах >
        Given search by loanhistory <nocustomercif>
    Then <no customer cif> completed
    Then <page-content> screen shot by class name <inquiry_loan_history_notfound_customer_negative>