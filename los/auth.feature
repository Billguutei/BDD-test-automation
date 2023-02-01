Feature: Check for login + & -

    Scenario: Login Fail
Given login url to RLOS
When we provide wrong authentication
Then error will show 

    Scenario: Login success
Given login url to RLOS
When we provide correct authentication
Then home page will load 

