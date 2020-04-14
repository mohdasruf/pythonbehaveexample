# Created by User at 07/04/2020
Feature: Sample integration test Demo

  Scenario: Download input file from S3 and trigger a python script
    Given I download the input file from S3 and place it in the test files folder
    And trigger the python script
    Then the output is as expected