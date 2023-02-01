Feature: Hamtran ajillagch baiguullagiin huu

    #Nemelteer 64 gesen role oor deeree nemj ogoh yostoi

    Scenario: Search-by-partner-organization-code
    
        Given login to ims
		    And <Search_by_partner_organization_code> load page
        Then <Search_by_partner_organization_code> loan interest of partner organization

    Scenario: Add-organization
    
        Given login to ims
		    And <Add_organization> load page
        Then <Add_organization> loan interest of partner organization