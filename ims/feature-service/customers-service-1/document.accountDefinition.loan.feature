Feature: Definition of Loan Account 


    Scenario: request approve 
        Given login to ims
		    And <document-definitionLoan> load page
            And create task
        Then approve task

    Scenario: request decline 
        Given login to ims
		    And <document-definitionLoan> load page
            And create task
        Then decline task

    Scenario: loan (outstanding)
        Given login to ims
		    And <document-definitionLoan> load page
            And create task
            And approve task
        When Do <approved-definitionLoan> to approved task
        Then <Өр зээлтэй (үлдэгдэлтэй)> choose type of definitionLoan
        Then <content> screen shot by class name <loan (outstanding)>

    Scenario:  have loan
        Given login to ims
		    And <document-definitionLoan> load page
            And create task
            And approve task
        When Do <approved-definitionLoan> to approved task
        Then <Өр зээлтэй эсэх> choose type of definitionLoan
        Then <content> screen shot by class name <have loan>
