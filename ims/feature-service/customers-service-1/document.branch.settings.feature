Feature: Upgrade to Branch 

    Scenario:  Upgrade to Branch 
        Given login to ims BUAA
		    And <document-upgradeBranch> load page
            And check page loaded <Миний салбарын мэдээллүүд>
            And click to upgrade button
        Then fill fields of branch upgrade
        Then <content> screen shot by class name <upgradeBranch>