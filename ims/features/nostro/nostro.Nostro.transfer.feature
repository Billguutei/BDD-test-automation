Feature: Nostro account 

    #104 gesen role nemj tawij ogno 

    Scenario: Ностро гүйлгээ 
        Given login to ims
            And <nostro_transfer> load page
        Then <Successed> nostro transfer
