Feature: Zeeliin huselt ilgeeh

    Scenario: loan request
        Given login to ims
            And <savings backed loan> load page
            And send to loan request
    Then <loan success> completed 