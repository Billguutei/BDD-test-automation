Feature: Гүйлгээний төрлөөр хайх

    Scenario: transaction type
        When <transaction list> load page
        Given search transaction <1010>
        Then <dataTables_wrapper> screen shot by class name <search_transaction_type>