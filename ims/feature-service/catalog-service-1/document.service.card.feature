Feature: Prepare document service card 

    Scenario: Дэд карт авах 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дэд карт авах > choose product of card

    Scenario: Дэд карт хаалгах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дэд карт хаалгах> choose product of card

    Scenario: Идэвхгүй карт нээлгэх 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Идэвхгүй карт нээлгэх > choose product of card

    Scenario: Карт нөхөн авах 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Карт нөхөн авах > choose product of card

    Scenario: Карт хаалгах 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Карт хаалгах > choose product of card

    Scenario: Картын бусад үйлчилгээ
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Картын бусад үйлчилгээ> choose product of card

    Scenario: Картын лимит нэмэгдүүлэх хүсэлт
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Картын лимит нэмэгдүүлэх хүсэлт> choose product of card

    Scenario: Картын нэр өөрчлүүлэх 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Картын нэр өөрчлүүлэх > choose product of card

    Scenario: Картын пин код өөрчлөх 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Картын пин код өөрчлөх > choose product of card

    Scenario: Картын хугацаа сунгуулах  
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Картын хугацаа сунгуулах > choose product of card

    Scenario: Орлогын карт авах 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Орлогын карт авах> choose product of card

    Scenario: Сурагчийн карт авах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Сурагчийн карт авах> choose product of card

    Scenario: Экспресс карт авах 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Экспресс карт авах > choose product of card