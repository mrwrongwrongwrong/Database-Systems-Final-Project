# db_project

This repository is for the purpose of Report of my implementations and final papers included in the assignment of final project in calss DB at NYU.

# Web Page
The main website of my design is at: https://yue201614.wixsite.com/csci-2433

Instructions: click on the 'Get Quota' button top left to get to the estimation of the acutal quota.

In case the 'Get Quota' button is not working in my web page, the back-up plan is: https://www.calconic.com/calculator-widgets/blank-calculator/611b7c41db5cac0021b82061?layouts=true 

# Model
The db_vanilla_multivariate_regression_model is the basic frameworks I used on my dataset with 12k datapoints. 

The independent variables are: 1.age, 2.race, 3.ethnicity, 4.gender, 5.latitude, 6.longitude. Hence I retrieved data[:,1:7] as my input variables. 

The dependent variable is: Healthcare_coverage. 

The column which has not been used is healthcare_expense. 

In our case, we adopt healthcare_coverage as insurance price, the health_expense is how much we are going to cover for the patient. 

The SGD_multivariate_regression_model is the upgraded version. It adapts the sotchatic gradient descent when the model is trainnined.

There are 500 iterations on each type of gradient descent, there are three types of gradient descents attempted: 1. gradient_descent 2. stochastic_gradient_descent 3. minibatch_gradient_descent


# Dataset
The dataset is on my personal google storage: https://storage.googleapis.com/dataprep-staging-b4c6b8ff-9afc-4b23-a0d8-d480526baaa4/yz1268%40nyu.edu/jobrun/Untitled%20recipe%20%E2%80%93%204.csv/2021-08-16_23-54-42_00000000

This is what after cleaning process has been done.

The original dataset is at synthea: https://synthea.mitre.org/downloads
