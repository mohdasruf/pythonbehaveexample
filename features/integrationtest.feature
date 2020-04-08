# Created by User at 07/04/2020
Feature: Sample integration test
  # Enter feature description here

  Scenario: End to end test
    Given I download the file and place it in the test files folder
    And trigger the python script
    Then the python output is as expected