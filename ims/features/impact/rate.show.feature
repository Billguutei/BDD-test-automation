Feature: Ханш харах

    Scenario: Тухайн өдрийн ханшийг харах
    When login to ims
    Given <rate show> load page
    Then <page-container> screen shot by class name <rates>