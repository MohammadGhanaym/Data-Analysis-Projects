## Overview (In Progress)
Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It helps businesses better understand their customers and makes it easier for them to modify products according to the specific needs, behaviors, and concerns of different types of customers.

By leveraging customer personality analysis, businesses can tailor their products based on target customer segments. Instead of marketing a new product to every customer in the database, companies can analyze which customer segment is most likely to buy the product and focus their marketing efforts accordingly.


## Data Gathering
In this project, I will use a dataset downloaded from [Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis).  
The dataset consists of **29 columns** and **2,240 rows**.

> According to the information in this [link](https://github.com/nailson/ifood-data-business-analyst-test/tree/master), this dataset is used for hiring Data Analysts for the iFood Brain team. It was last updated on **February 19, 2020**.

## Columns Description

### Customer Information
- **ID**: Customer's unique identifier  
- **Year_Birth**: Customer's birth year  
- **Education**: Customer's education level  
- **Marital_Status**: Customer's marital status  
- **Income**: Customer's yearly household income  
- **Kidhome**: Number of children in the customer's household  
- **Teenhome**: Number of teenagers in the customer's household  
- **Dt_Customer**: Date of customer's enrollment with the company  
- **Recency**: Number of days since the customer's last purchase  
- **Complain**: `1` if the customer complained in the last 2 years, `0` otherwise  

### Spending Behavior
- **MntWines**: Amount spent on wine in the last 2 years  
- **MntFruits**: Amount spent on fruits in the last 2 years  
- **MntMeatProducts**: Amount spent on meat in the last 2 years  
- **MntFishProducts**: Amount spent on fish in the last 2 years  
- **MntSweetProducts**: Amount spent on sweets in the last 2 years  
- **MntGoldProds**: Amount spent on gold in the last 2 years  

### Purchase Behavior
- **NumDealsPurchases**: Number of purchases made with a discount  
- **NumWebPurchases**: Number of purchases made through the company’s website  
- **NumCatalogPurchases**: Number of purchases made using a catalog  
- **NumStorePurchases**: Number of purchases made directly in stores  
- **NumWebVisitsMonth**: Number of visits to the company’s website in the last month  

### Campaign Response
- **AcceptedCmp1**: `1` if the customer accepted the offer in the 1st campaign, `0` otherwise  
- **AcceptedCmp2**: `1` if the customer accepted the offer in the 2nd campaign, `0` otherwise  
- **AcceptedCmp3**: `1` if the customer accepted the offer in the 3rd campaign, `0` otherwise  
- **AcceptedCmp4**: `1` if the customer accepted the offer in the 4th campaign, `0` otherwise  
- **AcceptedCmp5**: `1` if the customer accepted the offer in the 5th campaign, `0` otherwise  
- **Response**: `1` if the customer accepted the offer in the last campaign, `0` otherwise  


## Data Assessing

- The **`Income`** column contains **13 null values**.  
- The **`Dt_Customer`** column needs to be converted to the **Date** type.  
- **Unnecessary columns** for analysis: `Z_costContact`, `Z_revenue`.  

## Data Cleaning

1. Drop rows with missing values in the **`Income`** column.  
   - Since there are only **13 null values**, which is a very small proportion of the dataset, removing them is unlikely to significantly affect the analysis results.  

2. Convert the datatype of the **`Dt_Customer`** column to **Date** type.  
   - When I tried to change the type directly, I got an error because the data follows the **day-month-year** format. So, I converted it using the **Brazilian locale**, as this dataset is related to a food delivery app in Brazil, and it worked.  

3. Drop **unnecessary columns** for analysis: `Z_costContact`, `Z_revenue`.  

4. Create a new column named `AcceptedCmp` representing the number of offers that the customer has accepted.

5. Create a new column to represent the customer age name `Customer Age`
