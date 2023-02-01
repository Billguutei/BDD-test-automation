Feature: Nostro account 

    #104 gesen role nemj tawij ogno 

    Scenario: Ностро дансны зузаатгал 
        Given login to ims
            And <nostro_main> load page
        Then <MID_office_approve> nostro account 
        Then <nostro success> completed


 


