# db_project

This repository is for the purpose of Report of my implementations and final papers included in the assignment of final project in calss DB at NYU.

The main website of my design is at: https://yue201614.wixsite.com/csci-2433

Instructions: click on the 'get quota' button top left to get to the estimation of the acutal quota.

Or access: https://www.calconic.com/calculator-widgets/blank-calculator/611b7c41db5cac0021b82061?layouts=true 

The db_vanilla_multivariate_regression_model is the basic frameworks I used on my dataset with 12k datapoints. 
The independent variables are: 1.age, 2.race, 3.ethnicity, 4.gender, 5.latitude, 6.longitude. Hence I retrieved data[:,1:7] as my input variables. 
The dependent variable is: Healthcare_coverage. 
The column which has not been used is healthcare_expense. 
In our case, we adopt healthcare_coverage as insurance price, the health_expense is how much we are going to cover for the patient. 
