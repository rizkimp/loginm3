Feature: login & logout
  Scenario: login&logout using valid data
  Given go to homepage
  When click button login
  Then tooltip appear
  When input valid username & password & click login
  Then success login
