Feature: Банк дотор шилжүүлэг хийхэд хураамж авахгүй байгааг шалгах

    Банк Дотор Ажилтны данснаас энгийн данс-руу шилжүүлэг хийхэд хураамж авахгүй байгааг шалгах
    Scenario: domestic transfer nonfee
        Given login to ims
            And <4045> load page
            And create task
        When approve task
        Then <EMPLOYEE_ACCOUNT> transfer
        Then <transfer transaction> completed