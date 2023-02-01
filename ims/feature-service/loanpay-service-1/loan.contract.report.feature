Feature: Zeel gereenii tailan

    Scenario: Salary-loan-report
    
        Given login to ims
		    And <Salary_loan_report> load page
        Then <Salary_loan_report> loan contract report

    Scenario: Savings-loan-report 
    
        Given login to ims
		    And <Savings_loan_report> load page
        Then <Savings_loan_report> loan contract report