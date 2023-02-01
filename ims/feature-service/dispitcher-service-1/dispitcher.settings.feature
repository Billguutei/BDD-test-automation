Feature: Dispitcher auto transaction setting controller

    # Scenario: Choose from Account then fill to account fields and add account
    #     Given login to ims
    #         And <dispitcher> load page
    #     Then fill fields and <add account> 
    #     Then <adddispitcher> completed

    Scenario: Choose from Account then fill to account fields and add account
        Given login to ims
            And <dispitcher> load page
        Then fill fields and <add account transaction type external> 

    # Scenario: Choose from Account then update account date
    #     Given login to ims
    #         And <dispitcher> load page
    #     Then fill fields and <update> 

    # Scenario: Choose from Account then delete registered account
    #     Given login to ims
    #         And <dispitcher> load page
    #     Then fill fields and <delete> 