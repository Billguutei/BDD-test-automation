Feature: Zeel registereer haih

    Scenario: loan request
        Given login to ims
            And <savings backed loan> load page
            And loan search register
            Then <no-transitions> screen shot by class name <Loan_search_register>