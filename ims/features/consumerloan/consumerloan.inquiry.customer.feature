Feature: inquiry customer
    Scenario: inquiry customer search by null cif positive
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <null>
    Then <null cif customer> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_null_cif_negative>

    Scenario: inquiry customer search by cif positive
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <customercif>
    Then <page-content> screen shot by class name <inquiry_customer_by_cif_positive>

    Scenario: inquiry customer search by string register or cif negative
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <wrongvalue1>
    Then <no customer cif> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_string_register_cif_negative>

    Scenario: inquiry customer search by numeric register negative
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <wrongvalue2>
    Then <no customer cif> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_numericregister_negative>

    Scenario: inquiry customer search by cif without check digit negative
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <nocheckdigit>
    Then <no customer cif> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_nocheckdigit_cif_negative>

    Scenario: inquiry customer search by not found cif negative
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <notfound cif>
    Then <no customer cif> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_notfound_cif_negative>

    Scenario: inquiry customer search by not found register in bancs negative
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <emptyregister>
    Then <empty register> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_notfound_cif_negative>

    Scenario: inquiry customer search by not found register negative
        When login to ims
            And <consumerloan-lavlagaa> load page
            And check page loaded < Лавлагаа >
        Given search by loanhistory <notfound reg>
    Then <no customer cif> completed
    Then <page-content> screen shot by class name <inquiry_customer_by_notfound_reg_negative>
     