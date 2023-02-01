Feature: Prepare document Internet Bank 

    Scenario: Cancel to Ebilling service
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <И-Биллинг үйлчилгээ цуцлах> choose product of cyber

    Scenario: Change to email of Internet bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны  и-мэйл хаяг солиулах> choose product of cyber


    Scenario: limit up to Internet Bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны  лимит нэмэгдүүлэх> choose product of cyber

    Scenario: change to phone numner of Internet Bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны Утасны дугаар солиулах> choose product of cyber

    Scenario: Get VASCO of Internet Bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны васко төхөөрөмж авах> choose product of cyber


    Scenario: reset and change to password of Internet Bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны нууц үг сэргээх, солиулах> choose product of cyber


    Scenario: Recover to Internet Bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны үйлчилгээ сэргээх> choose product of cyber

    Scenario: Cancel to Internet Bank
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Интернэт банкны үйлчилгээ цуцлах> choose product of cyber

    Scenario: Recover to Mobile Banking Service 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банк үйлчилгээг сэргээх> choose product of cyber


    Scenario: Cancel to Mobile Banking Service 
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банк үйлчилгээг цуцлах> choose product of cyber

    Scenario: Change phone number of Mobile banking Service
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банк-Утасны дугаар солиулах> choose product of cyber

    Scenario: Recover active code of Mobile Banking , Add Account
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банкны идэвхижүүлэлтийн код сэргээх, данс нэмэх> choose product of cyber

    Scenario: Limit up to Mobile Banking
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банкны лимит нэмэгдүүлэх> choose product of cyber

    Scenario: Recover,Reset Password of Mobile Banking Service
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банкны нууц үг солиулах, сэргээлгэх> choose product of cyber


    Scenario: Мобайл банкны үйлчилгээ сунгах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Мобайл банкны үйлчилгээ сунгах> choose product of cyber


    Scenario: Телефон банкны лимит нэмэгдүүлэх
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Телефон банкны лимит нэмэгдүүлэх> choose product of cyber

    Scenario: Телефон банкны үйлчилгээ цуцлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Телефон банкны үйлчилгээ цуцлах> choose product of cyber

    Scenario: Ухаалаг мэдээ үйлчилгээг цуцлах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Ухаалаг мэдээ үйлчилгээг цуцлах> choose product of cyber
 
    Scenario: Ухаалаг мэдээ, Мэдээллийн төрөл солиулах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Ухаалаг мэдээ, Мэдээллийн төрөл солиулах> choose product of cyber

    Scenario: Ухаалаг мэдээ, утасны  дугаар солиулах
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Ухаалаг мэдээ, утасны  дугаар солиулах> choose product of cyber
 
    Scenario: Цахим банкны бусад үйлчилгээ
        Given login to ims
		    And <document-service> load page
            And create task
            And approve task
        When Do <approved-document> to approved task
        Then <Цахим банкны бусад үйлчилгээ> choose product of cyber
