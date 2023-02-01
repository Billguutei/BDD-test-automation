Feature: Prepare document service create account corporate

    Scenario: .Данс нээх 1 - Corporate
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <.Данс нээх 1> choose product  of corp account

    Scenario: .Данс нээх 2 - Corporate
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <.Данс нээх 2> choose product  of corp account
    
    Scenario: .Данс нээх 3 - Corporate
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <.Данс нээх 3> choose product  of corp account

    Scenario: Тусгай урьдчилсан хүүт хадгаламж /2223-1/
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Тусгай урьдчилсан хүүт хадгаламж /2223-1/> choose product  of corp account

    Scenario: Тусгай харилцах 
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Тусгай харилцах > choose product  of corp account

    Scenario: Тусгай хугацаагүй хадгаламж /1001-2 1011-2 1021-2/
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Тусгай хугацаагүй хадгаламж /1001-2 1011-2 1021-2/> choose product  of corp account

    Scenario: Тусгай хугацаатай хадгаламж /2400-3 2410-3/
    #zaswar hiinee ims dre aldaatai bga
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Тусгай хугацаатай хадгаламж /2400-3 2410-3/> choose product  of corp account
    
    Scenario: Хадгаламжийн сертификат /2700-1,2/
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Хадгаламжийн сертификат /2700-1,2/> choose product  of corp account
    
    Scenario: Эскроу харилцах /3000-17 3010-17 3013-17/
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Эскроу харилцах /3000-17 3010-17 3013-17/> choose product  of corp account
    
    Scenario: Үнэт цаасны арилжааны эскроу /3000-26/
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Үнэт цаасны арилжааны эскроу /3000-26/> choose product  of corp account
    
    Scenario: Бизнес карт авах
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Бизнес карт авах> choose product  of corp account

    Scenario: И-Биллинг үйлчилгээ авах
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <И-Биллинг үйлчилгээ авах> choose product  of corp account

    Scenario: Интернэт банкны гүйлгээний зөвшөөрлийн зэрэг тохируулах 
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны гүйлгээний зөвшөөрлийн зэрэг тохируулах > choose product  of corp account
    
    Scenario: Интернэт банкны үйлчилгээ авах
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны үйлчилгээ авах> choose product  of corp account
    
    Scenario: Свип үйлчилгээ авах 
        Given login to ims
		    And <document-service> load page
            And create organization task
            And approve task
        When Do <approved-document> to approved task
        Then <Свип үйлчилгээ авах > choose product  of corp account
