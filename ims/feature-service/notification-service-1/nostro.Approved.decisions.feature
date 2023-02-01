Feature: Nostro account 

    #104 gesen role nemj tawij ogno 

    Scenario: Зөвшөөрөгдсөн шийдвэрүүд  
        Given login to ims
            And <nostro_approved> load page
        Then nostro approved decisions
        Then <nostro success> completed
