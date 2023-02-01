Feature: unsuccessful transaction

    Scenario: find transaction type failed transaction
        Given login to ims
            And <transaction list> load page
            And check page loaded <Гүйлгээний жагсаалт>
        When <unsuccessful> transaction list 
        Then <dataTables_wrapper> screen shot by class name <transaction_list_unsuccessful>

    Scenario: find date transaction
        Given login to ims
            And <transaction list> load page
            And check page loaded <Гүйлгээний жагсаалт>
        When <date> transaction list 
        Then <dataTables_wrapper> screen shot by class name <transaction_list_date>