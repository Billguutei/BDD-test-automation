Feature: Ханшийн түүх

    Scenario: Шинэчлэгдсэн ханшийн мэдээлэл
    When login to ims
    Given <rate history> load page
    And <Шинэчлэгдсэн ханшийн мэдээлэл> find date
    Then <datatable-scroll> screen shot by class name <modified-rate>
    
    Scenario: Хүлээгдэж буй ханшийн мэдээлэл
    When login to ims
    Given <rate history> load page
    And <Хүлээгдэж буй ханшийн мэдээлэл> find date
    Then <datatable-scroll> screen shot by class name <waiting-rate>

