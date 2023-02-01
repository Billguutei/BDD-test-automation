Feature: Prepare document service account 

    Scenario: Баталгаат гарын үсэг шинэчлэх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Баталгаат гарын үсэг шинэчлэх> choose product of account service

    Scenario: Буруу үүссэн, давхардсан CIF засварлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Буруу үүссэн, давхардсан CIF засварлах> choose product of account service
   
    Scenario: Данс лавлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Данс лавлах> choose product of account service
   
    Scenario: Close Account
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Данс хаах> choose product of account service
   
    Scenario: Дансанд зогсоолт хийх 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансанд зогсоолт хийх > choose product of account service

    Scenario: Дансанд хамтран эзэмшигч бүртгэх болон нэмэх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансанд хамтран эзэмшигч бүртгэх болон нэмэх> choose product of account service
  
    Scenario: Дансны барилт цуцлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны барилт цуцлах> choose product of account service
  
    Scenario: Дансны бусад үйлчилгээ
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны бусад үйлчилгээ> choose product of account service

    Scenario: Дансны төлөв өөрчлөх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны төлөв өөрчлөх> choose product of account service

    Scenario: Дансны төрөл, категори солих
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны төрөл, категори солих> choose product of account service

    Scenario: Дансны хамтран эзэмшигч цуцлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны хамтран эзэмшигч цуцлах> choose product of account service

    Scenario: Get Account Statement
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны хуулга авах> choose product of account service

    Scenario: Дансны үлдэгдэлд барилт хийх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Дансны үлдэгдэлд барилт хийх> choose product of account service

    Scenario: Зогсоолт чөлөөлөх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Зогсоолт чөлөөлөх> choose product of account service

    Scenario: Харилцагчийн CIF идэвхжүүлэх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Харилцагчийн CIF идэвхжүүлэх> choose product of account service

    Scenario: Харилцагчийн сегмент, төрөл солих
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Харилцагчийн сегмент, төрөл солих> choose product of account service

    Scenario: Хугацаатай хадгаламжийн хугацаа сунгах захиалга /2071/
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Хугацаатай хадгаламжийн хугацаа сунгах захиалга /2071/> choose product of account service

    Scenario: Хуримтлал цуцлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Хуримтлал цуцлах> choose product of account service

    Scenario: Хуримтлалын үйлчилгээ засварлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Хуримтлалын үйлчилгээ засварлах> choose product of account service
