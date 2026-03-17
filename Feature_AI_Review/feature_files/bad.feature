Feature: login
Background:
When user opens login page
Given user enters username
And user enters password

@Priority-5
Scenario: Login test

Given user clicks login
Then dashboard appears