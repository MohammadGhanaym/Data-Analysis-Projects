# Overview
We will be analyzing a fictitious churn dataset from a Telecom provider called Databel to know why customers are churning.
The Databel dataset consists of 29 columns with one row per customer. We'll be analyzing a snapshot of the database at a specific time, meaning there is no time dimension.
If you want to know more about the data check out the `Metadata Sheet - Customer Churn` file. 
There are two sheets:
- Databel - Customer
- Databel - Aggreate: The aggregate views are based on data in Databel - Customer.



### Analysis Steps
- First, I extracted the data into a view table and checked for duplicate values; there were none.
- Then, we created a new column called `Churned` from the `Churn Label` column using an IF statement, assigning 1 for "Yes" and 0 for "No."
- We created a blank PivotTable of the Customers table, placed it in a new Worksheet, and renamed it "Customer Pivots".
    - Then, we calculated the total number of customers and the number of churned customers.
    - Then, we calculated the churn rate by dividing the number of churned customers by the total number of customers.
- We found that 26.86% of the customers churned which is fairly high.
- After that, we started to investigate why customers churned
    - We created a new pivot table to analyze the total number of churned customers by Churn Reason.
    - We calculated the churned customers by reason as a percentage of the total churned customers
    - We created a bar chart to visualize the results
    - We found that the top 3 reasons of customer churn reasons are:
        - Competitor made better offer
        - Competitor had better devices
        - Attitude of support person

