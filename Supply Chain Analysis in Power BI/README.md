# Overview
In this project, we will analyze supply chain data to optimize shipping operations and enhance the customer delivery experience. Our analysis will focus on shipping performance and timeliness, customer delivery behavior across regions, and the relationship between sales performance and shipping efficiency.

![dashboard.gif](Vis/Dashboard.gif)
We will try to answer questions like:
- Which region and market have the highest number of late product deliveries?  
- Which region and store generate the highest profit?  
- Are late orders related to specific departments?  
- Which region has the highest number of orders?  
- Do you have customer churn? 
- What are the order trends over time?  
- Is there a relationship between discounts and low profit?  
- Which customer segments generate the highest profit?

# Data Gathering
You can download the dataset from this link: [DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS
](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis/data)

#### Dataset Fields and Descriptions

| **Field**                         | **Description**                                                                                   |
|----------------------------------|---------------------------------------------------------------------------------------------------|
| `Type`                           | Type of transaction made                                                                          |
| `Days for shipping (real)`       | Actual shipping days of the purchased product                                                     |
| `Days for shipment (scheduled)`  | Days of scheduled delivery of the purchased product                                               |
| `Benefit per order`              | Earnings per order placed                                                                         |
| `Sales per customer`             | Total sales per customer                                                                          |
| `Delivery Status`                | Delivery status of orders: Advance shipping, Late delivery, Shipping canceled, Shipping on time  |
| `Late_delivery_risk`             | Categorical variable: 1 if late, 0 if not late                                                    |
| `Category Id`                    | Product category code                                                                             |
| `Category Name`                  | Description of the product category                                                               |
| `Customer City`                  | City where the customer made the purchase                                                         |
| `Customer Country`               | Country where the customer made the purchase                                                      |
| `Customer Email`                 | Customer's email                                                                                  |
| `Customer Fname`                 | Customer's first name                                                                             |
| `Customer Id`                    | Customer ID                                                                                       |
| `Customer Lname`                 | Customer's last name                                                                              |
| `Customer Password`              | Masked customer key                                                                               |
| `Customer Segment`              | Customer type: Consumer, Corporate, Home Office                                                   |
| `Customer State`                 | State of the store location where purchase is registered                                          |
| `Customer Street`                | Street of the store location where purchase is registered                                         |
| `Customer Zipcode`               | Customer Zipcode                                                                                  |
| `Department Id`                  | Store department code                                                                             |
| `Department Name`                | Store department name                                                                             |
| `Latitude`                       | Latitude of store location                                                                        |
| `Longitude`                      | Longitude of store location                                                                       |
| `Market`                         | Market region: Africa, Europe, LATAM, Pacific Asia, USCA                                          |
| `Order City`                     | Destination city of the order                                                                     |
| `Order Country`                  | Destination country of the order                                                                  |
| `Order Customer Id`              | Customer order code                                                                               |
| `Order Date (DateOrders)`        | Date on which the order is made                                                                   |
| `Order Id`                       | Order code                                                                                        |
| `Order Item Cardprod Id`         | Product code generated through RFID                                                               |
| `Order Item Discount`            | Order item discount value                                                                         |
| `Order Item Discount Rate`       | Order item discount percentage                                                                    |
| `Order Item Id`                  | Order item code                                                                                   |
| `Order Item Product Price`       | Price of product without discount                                                                 |
| `Order Item Profit Ratio`        | Order item profit ratio                                                                           |
| `Order Item Quantity`            | Number of products per order                                                                      |
| `Sales`                          | Value in sales                                                                                    |
| `Order Item Total`               | Total amount per order                                                                            |
| `Order Profit Per Order`         | Profit per order                                                                                  |
| `Order Region`                   | Delivery region: Southeast Asia, West USA, Central Africa, Europe, etc.                          |
| `Order State`                    | Delivery state                                                                                    |
| `Order Status`                  | Order status: COMPLETE, PENDING, CLOSED, etc.                                                     |
| `Product Card Id`                | Product code                                                                                      |
| `Product Category Id`            | Product category code                                                                             |
| `Product Description`            | Product description                                                                               |
| `Product Image`                  | Link to product image or page                                                                     |
| `Product Name`                   | Product name                                                                                      |
| `Product Price`                  | Product price                                                                                     |
| `Product Status`                 | Product availability: 1 = Not available, 0 = Available                                            |
| `Shipping Date (DateOrders)`     | Exact date and time of shipment                                                                   |
| `Shipping Mode`                  | Shipping mode: Standard Class, First Class, Second Class, Same Day                                |


# Data Assessing
 
Let's assess the data and identify potential issues.  
- There are 180,519 rows and 53 columns.  
- There are no duplicate rows.
- 97% of `Order Zipcode` is empty and `Product Description` has no data.
- The `Customer Email` and `Customer Password` columns contain only one value: `XXXXXXXXX`.  
- The `Product Status` column contains only one value: `0` = `Available`.  
- This table contains information about orders and their items, which means there are duplicate order IDs (one order can appear multiple times for different items).
- `Benefit per order` and `Order Profit Per Order` have the same data.
- `Sales per customer` and `Order Item Total` have the same data.
- We are going to create tables for `FactOrders`, `DimCustomer`, `DimProduct`, `DimGeography`, `DimDepartment`, and `DimDate` so that we can build a Star schema or a Snowflake schema.

# Data Cleaning

- Drop unnecessary columns such as `Order Zipcode`, `Customer Email`, `Customer Password`, `Product Description` and `Product Status`.  
- Drop `Benefit per Order` and `Sales per Customer` since they contain information already in other columns.
- Create `Full Name` column in `DimCustomer`
- Create the data model:

![image.png](Vis/95f11686-f2c7-42e6-b752-02461050f98a.png)

# Exploratory Data Analysis

## Overview
![image.png](Vis/dd071b63-5b12-484d-b759-089f6a3debcb.png)

![image.png](Vis/bd33af71-c9f1-489c-925e-90e750d284f9.png)
- There are 64K total orders and 19K unique customers.
- The total revenue is \\$32.76M, and the total profit is \\$3.93M, resulting in a 12.01% profit margin.
- The total discount amount is \\$3.7M, which is very close to the total profit.

![image.png](Vis/3ad004ff-80da-4c75-b623-50dc08771afe.png)
- We can see that the most profitable store is the one that offers more discounts.

![image.png](Vis/cf5d423e-8673-4342-8134-8dc223881338.png)
- Total profit remained consistent over the years; however, the profit margin slightly increased in 2017.
- 2018 does not have data for the entire year; therefore, we will exclude it from this analysis.

![image.png](Vis/7076fda3-0886-43b9-870a-985ec5fe801e.png)

- Most of the orders are delivered late. We need to investigate further way this happens and I think we can use this dataset to create a better model that good estimate the delivery date for future orders.

![image.png](Vis/086a20c5-60bf-4169-bd96-8333fde4475b.png)

- Most of the profit comes from orders going to countries in Europe and LATAM.
- Africa has the lowest profit.

![image.png](Vis/e4eb95b0-f2dc-46aa-a405-c1ed434d6634.png)

- We observe numerous orders directed to European countries, including France, Germany, and the United Kingdom. Additionally, many orders are sent to Central and South America, as well as the USA. In Asia, the majority of orders go to India, China, and Indonesia.
- Africa experiences a low volume of orders, which accounts for its minimal profit.


## Customer
![image.png](Vis/82da390b-0202-40b4-bdb9-0049e92903e7.png)

![image.png](Vis/a38f22d7-3e52-45c6-a911-ebeb96d5474c.png)
- Customers increased significantly in 2017, from 10K in 2016 to 15K in 2017 — a 50% increase.

![image.png](Vis/87e66775-cf1e-4913-b239-b1b8893c61e7.png)
- Montana (MT) has the lowest percentage of late orders but only accounts for 10 customers and 31 orders.
- In contrast, the District of Columbia (DC), Delaware (DE), and New Mexico (NM) have the highest percentages of late orders, despite having relatively low volumes of customers and orders.
- On the other hand, Puerto Rico (PR) and California (CA) have significantly higher volumes of customers and orders, yet maintain lower percentages of late orders—even though the overall late order rate remains high at 54%.

![image.png](Vis/92e6dc7e-e875-4b99-97d4-a4e671225055.png)
- We can't conclude that late orders are due to a specific customer segment, as there is no significant difference in the percentage of late orders among the segments.

![image.png](Vis/9f05625c-cbd9-476f-9fb2-74d79d9df5cc.png)
- Most of our customers are from the Consumer segment.

![image.png](Vis/d0c5c891-2ef2-48b8-bdef-0cedff4c5486.png)
- The Consumer segment generates the largest profit. This is because most of our customers belong to the Consumer segment.

## Product

![image.png](Vis/6deb196b-c327-4955-ad05-442ddab2501e.png)

![image.png](Vis/9aefde30-244c-40d2-a2c7-4f863572b0e0.png)
- There are 118 unique products and 51 categories, and the number of sold items is 178K.

![image.png](Vis/9e444bff-5749-439c-8df2-7c104953c916.png)
- Electronics category has the largest number of products.

![image.png](Vis/f6031c09-e240-45bc-b411-110209e4d513.png)
- Cleats category has the largest number of sold items despite it has only 2 products.

![image.png](Vis/be1345aa-3940-4bdc-96d7-751a0d3006ec.png)
- Items from the Golf Bags & Carts category are the most likely to be delivered late.

![image.png](Vis/bb8fb8ce-7a10-4833-9bf5-450c77cb4488.png)
- Number of sold products decreased in 2017 compared to 2016 and 2015

![image.png](Vis/a93dce29-76f2-443e-b4d0-aa62d1a573c3.png)
- The Fishing category generates the highest profit.

- The Cleats category has the highest number of products sold, but it generates less profit than the Fishing category.

## Geography

![image.png](Vis/53b4b643-87ed-481b-9ab1-e2766fa20ccd.png)

![image.png](Vis/a00247d4-0a87-4346-b4ad-559a4a6fd572.png)
- We delivered orders to 162 country out of 192 country from 11 stores.

![image.png](Vis/6aaf3c2f-25a2-4796-b2dc-3aba3ddc832a.png)
- Countries with high orders also experience a late delivery percentage close to the overall percentage of late orders.

![image.png](Vis/eb7940aa-5748-4d6c-98a9-7426a1dace1e.png)
- In this chart, we can see that late deliveries do not necessarily result in low revenue. On the contrary, countries like Canada, which have the lowest percentage of late orders, generate the lowest profit. On the other hand, Central America and Western Europe generate the highest profit despite having a higher percentage of late orders.

![image.png](Vis/f5ba7dde-8cf1-48b1-af70-5f62fe2e7084.png)
- Europe generates the highest revenue, while Africa generates the least.

![image.png](Vis/c10793e6-191a-4e02-9869-ac5b6511dd2f.png)
- Within Europe, Western Europe generates the highest revenue, while Eastern Europe generates the least.

![image.png](Vis/05b4d2d8-273d-4f28-867d-cc5aa37c8f4e.png)
- Central America generates the highest revenue in the LATAM market.

![image.png](Vis/54a7fbda-7623-4916-91e3-406cbdd94667.png)
- Southeast Asia generates the highest revenue in the Pacific Asia market.

![image.png](Vis/3431c9f8-e59e-4b6d-84f2-efcb153687d8.png)
- The Western USA region generates the highest revenue, while Canada generates the least in the USCA market.

![image.png](Vis/1f81bcc9-fe66-43e4-8305-4cd38b75812a.png)
- West Africa generates the highest revenue in the African market.

## Order Delay
On this page, we can track the delayed orders. We can filter by state and market to view delayed orders by country, department, customer segment, and product category for each state and market.

![image.png](Vis/3db82061-371c-4264-8080-c98bbaed4321.png)

![image.png](Vis/500641b6-61b7-45bd-bde5-4801ba725157.png)

- The number of orders slightly increased in 2017, while the percentage of late orders remained approximately the same. 

![image.png](Vis/cc26d2f6-5fcd-47f8-ae96-449fece89739.png)
- The Fan Shop generates the highest profit and has a moderate percentage of late orders compared to other stores.

- The Pet Shop has the highest percentage of late orders and generates low profit.

- Therefore, we cannot conclude that late orders necessarily lead to low profit.

![image.png](Vis/d0bff6a6-25ad-4274-b0bf-4b9edd03db83.png)
- If we filter by customers **who purchased orders from California and had them delivered to Europe**, we observe that the number of orders dropped in 2016 and then increased in 2017. The percentage of late orders has remained consistent over the years. Furthermore, the Pet Shop has the highest percentage of late orders (100%), while the Discs Shop has the lowest (50%).

- When examining product categories, the Pet Supplies category has the highest percentage of late orders, which aligns with the Pet Shop store data mentioned earlier. In contrast, the Baseball & Softball category has the lowest percentage (35.29%).

- The Consumer segment has a slightly higher percentage of late orders compared to the other segments.

# Conclusions
- There are 64K total orders and 19K unique customers.

- The total revenue is \\$32.76M, and the total profit is \\$3.93M, resulting in a 12.01% profit margin.

- The total discount amount is $3.7M, which is very close to the total profit.

- 54.78% of orders were delivered late.

- We investigated whether late deliveries result in low profit, but found no patterns to support that. On the contrary, countries with a high or moderate percentage of late orders often generate high profit, likely due to the high volume of orders delivered to those regions.

- Customer segments show no strong relationship with late delivery. Most of our customers fall under the Consumer segment, which also generates the highest profit.

- The number of customers increased significantly in 2017 compared to 2016, but there appears to be some customer churn, as we have only around 15K active customers in 2017 despite having a total of 19K customers overall.

- There is a positive linear relationship between discounts and profit — higher discounts are correlated with higher profit.
