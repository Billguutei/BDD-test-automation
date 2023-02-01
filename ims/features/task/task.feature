Feature: Task

    #Давуу эрхтэй БҮА юм уу Ахлах БҮА -н роль-г нэмж өгөх шаардлагатай

    Scenario: Миний үүсгэсэн ажлууд 
    
        Given login to ims
		    And <My_create_task> load page
            And check page loaded <Миний үүсгэсэн ажлууд>
            Then task menus filter <OPEN>
            And <My_create_task> load page
            Then task menus filter <APPROVED>
            And <My_create_task> load page
            Then task menus filter <RESLVD>
            And <My_create_task> load page
            Then task menus filter <CLOSED>

    Scenario: Багт хувиарлагдсан ажлууд 
    
        Given login to ims
		    And <Assigned_to_team> load page
            And check page loaded <Ажлын жагсаалт>
            Then task menus filter <OPEN>
            And <Assigned_to_team> load page
            Then task menus filter <APPROVED>
            And <Assigned_to_team> load page
            Then task menus filter <RESLVD>
            And <Assigned_to_team> load page
            Then task menus filter <CLOSED>

    Scenario: Надад хувиарлагдсан ажлууд 
    
        Given login to ims
		    And <Assigned_to_me> load page
            And check page loaded <Надад хувиарлагдсан ажлууд>
            Then task menus filter <OPEN>
            And <Assigned_to_me> load page
            Then task menus filter <APPROVED>
            And <Assigned_to_me> load page
            Then task menus filter <RESLVD>
            And <Assigned_to_me> load page
            Then task menus filter <CLOSED>
    

         