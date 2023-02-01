Feature: 13000

  Scenario: 13000 inquiry positive
    When login to ims
      And <13000> load page
      And check page loaded <Зээлийн дансны лавлагаа>
    Given <13000> fill field <LOAN_ACCOUNT>
      And create task
      And approve task
    Then <dialog-body> screen shot <13000>
