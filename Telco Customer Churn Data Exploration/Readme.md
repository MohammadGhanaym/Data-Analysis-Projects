## Which dataset I chose?

 [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn) from Kaggle

This data contains 7043 rows (customers) and 21 columns (features).
The data set includes information about:
- Customers who left within the last month – the column is called Churn
- Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers – gender, age range, and if they have partners and dependents

## Main findings from the exploratory data analysis

- Data is imbalanced since customers who didn't leave in the last month represent 73.51%.
- There is not a large difference between the number of males and females since the number of males represents 50.43% and the number of females represents 49.57%.
- Most of the customers are not senior citizens since senior citizen customers only represent 83.72%.
- There is not a large difference between the number of customers who have a partner and those who are not. Since the number of customers that have a partner represents 48.40%, and those who are not; represent 51.60%.
- Most of the customers have dependents since they represent 70.06% of the customers.
- There is a large number of customers that only stayed with the company for one month.
- Most of the customers have a phone service since they represent 90.30% of the customers.
- 34.44% of the customers have an internet service provider of type DSL.
- 44.08% of the customers have an internet service provider of type fiber optic.
- 21.48% of the customers don't have an internet service provider.
- Most of the customers don't have tech support since they represent 49.42% of the customers.
- 29.10% of the customers have tech support. 
- 21.48% of the customers don't have internet service.
- Most of the customers have a month-to-month contract term since they represent 54.96% of the customers.
- 21% of the customers have a one-year contract term.
- 24.04% of the customers have a two-year contract term.
- 33.65% of customers use electronic checks as their payment method.
- 22.65% of the customers use mailed checks.
- 22% of the customers use bank transfers.
- 21.70% of the customers use credit cards.
- The distribution of the MonthlyCharges column is right-skewed.
- There is a large number of customers that the amount charged to them monthly is less than 30.
- The distribution of the TotalCharges column is right-skewed.
- Most of the customers have a total amount charged less than 2000.

- The proportions of males and females who leave the company are approximately the same. And it's the same for those who don't leave. This didn't give us any useful information that could help us know what affects the Churn.
- 64.01 % of customers are young and don't leave the company.
- 19.71 % of customers are young and leave the company.
- 9.50 % of customers are senior citizens and don't leave the company.
- 6.78% of customers are senior citizens and leave the company.
- More than half of the customers are young and don't leave the company.
- We can't say most of the customers who leave the company are young. This is because the data is imbalanced since the number of young customers is greater than senior citizens. If the number of young customers and senior citizens is the same, It will be a fair comparison.
- 38.86% of customers have partner and don't leave the company.
- 9.54% of customers  have partner and leave the company.
- 34.65% of customers don't have partner and don't leave the company.
- 16.95% of customers don't have partner and leave the company.
- 48.22% of customers don't have dependents and don't leave the company.
- 21.84% of customers don't have dependents and leave the company.
- 25.29% of customers have dependents and don't leave the company.
- 4.65% of customers have dependents and leave the company.
- About half of the customers don't have dependents and don't leave the company. And this is because most of the customers are young, and young people usually don't have dependents.
- Most of the customers who leave the company don't stay more than 20 months with the company.
- The customers who don't leave the company stay with the company for 38 months in the median.
- 7.28% of customers don't have phone service and don't leave the company.
- 2.43% of customers don't have phone service and leave the company.
- 66.23% of customers have phone service and don't leave the company.
- 24.07% of customers have phone service and leave the company.
- More than half of the customers have phone service and don't leave the company.
- 27.92% of the customers have an internet service provider of type DSL and don't leave the company.
- 6.52% of the customers have an internet service provider of type DSL and leave the company.
- 25.66% of the customers have an internet service provider of type fiber optic and don't leave the company.
- 18.42% of the customers have an internet service provider of type fiber optic and leave the company.
- 19.93% of the customers don't have an internet service and don't leave the company.
- 1.55% of the customers don't have an internet service and leave the company.
- Most of the customers that leave the company have internet service providers of type fiber optic.
- 28.90% of the customers don't have tech support and don't leave the company.
- 20.51% of the customers don't have tech support and leave the company.
- 24.68% of the customers have tech support and don't leave the company. 
- 4.42% of the customers have tech support and leave the company. 
- Most of the customers that leave the company don't have tech support.
- 31.53% of the customers have a month-to-month contract term and don't leave the company.
- 23.44% of the customers have a month-to-month contract term and leave the company.

- 18.63% of the customers have a one-year contract term and don't leave the company.
- 2.37% of the customers have a one-year contract term and leave the company.

- 23.35% of the customers have a two-year contract term and don't leave the company.
- 0.68% of the customers have a two-year contract term and leave the company.

- Most customers that leave the company have a month-to-month contract term.
- 18.46% of customers use electronic checks as their payment method and don't leave the company.
- 15.19% of customers use electronic checks as their payment method and leave the company.

- 18.35% of the customers use mailed checks and don't leave the company.
- 4.31% of the customers use mailed checks and leave the company.

- 18.32% of the customers use bank transfers and don't leave the company.
- 3.68% of the customers use bank transfers and leave the company.

- 18.39% of the customers use credit cards and don't leave the company.
- 3.31% of the customers use credit cards and leave the company.

- Most customers that leave the company use electronic checks.
- The median amount charged monthly to the customers who leave the company is 79.7.
- The median amount charged monthly to the customers who don't leave the company is 64.55.
- For most customers who don't leave the company, the amount charged to them monthly is less than or equal to 20.
- For most customers who leave the company, the amount charged to them monthly is approximately between 80 and 100.
- The median total amount charged to the customers who leave the company is 713.1.
- The median total amount charged to the customers who don't leave the company is 1688.9.
- For most customers who don't leave the company, the total amount charged to them is approximately between 19 and 2000.
- For most customers who don't leave the company, the total amount charged to them is approximately between 20 and 800.
- Most young customers who leave the company don't stay more than 20 months with the company. It's the same for senior citizen customers.
- Regardless of was the customer is a young or senior citizen, the customers who stayed a few months are more likely to leave the company. And the customers who stayed for more than 35 months are more likely to stay with the company.
- Customers who had a partner are most likely to stay if they stayed with the company for more than 60 months, and they are more likely to leave if they stayed with the company for less than 20 months.
- Customers who didn't have dependents are most likely to leave if they stayed with the company for less than 20 months. This distribution is very similar to the distribution of senior citizens by tenure and churn. This is because young customers didn't have dependents, and senior citizens had dependents.
- The customers who stayed for about 45 months on average with the company and had an internet service provider of type fiber optic are more likely to stay with the company.
- The customers who stayed for about 20 months on average with the company and had an internet service provider of type fiber optic are more likely to leave the company.

- The customers who stayed for about 15 months on average with the company and had an internet service provider of type DSL are more likely to leave the company.
- The customers who stayed for more than 40 months on average with the company and had tech support are more likely to stay with the company.
- The customers who stayed for less than 18 months on average with the company and didn't have tech support are more likely to leave the company.

#### How you chose the results to put in your explanatory analysis.

I chose the results that related to the Churn column which is our feature of interest.
