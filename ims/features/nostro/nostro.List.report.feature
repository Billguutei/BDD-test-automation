Feature: Nostro account 

    #104 gesen role nemj tawij ogno 

    Scenario: Ностро жагсаалт тайлан 
        Given login to ims
            And <nostro_report> load page
        Then <Shiidveruud> nostro list report


