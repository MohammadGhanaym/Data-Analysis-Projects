# Overview
In this analysis, I will help a computer hardware company evaluate the performance of its sales teams and agents and identify which products have the highest win rates. By analyzing key metrics such as total bookings, average deal size, win rate, and time to close, we will uncover actionable insights to improve sales performance, reduce lost opportunities, and drive profitability.

																																																		
![image.png](Visualizations/8c4e71f3-edb8-435f-9b02-26ead5406bd4.png)


## **Data Gathering**

- We downloaded the dataset from [Maven Analytics](https://mavenanalytics.io/data-playground?accessType=open&dataStructure=Multiple%20tables&order=date_added%2Cdesc&tags=Business&tags=Retail), and it is provided in CSV file format.  
- We extracted the data and imported it into an Excel sheet for analysis.

### **Datasets Description**
The data we have consists of 4 tables: accounts, products, sales_pipeline, and sales_teams tables

#### **Accounts Table**
| Field             | Description                          |
|-------------------|--------------------------------------|
| account           | Company name                         |
| sector            | Industry                             |
| year_established  | Year Established                     |
| revenue           | Annual revenue (in millions of USD)  |
| employees         | Number of employees                  |
| office_location   | Headquarters                         |
| subsidiary_of     | Parent company                       |

---

#### **Products Table**
| Field         | Description                  |
|---------------|------------------------------|
| product       | Product name                 |
| series        | Product series               |
| sales_price   | Suggested retail price       |

---

#### **Sales Teams Table**
| Field           | Description                  |
|-----------------|------------------------------|
| sales_agent     | Sales agent                  |
| manager         | Respective sales manager     |
| regional_office | Regional office              |

---

#### **Sales Pipeline Table**
| Field           | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| opportunity_id  | Unique identifier                                                           |
| sales_agent     | Sales agent                                                                 |
| product         | Product name                                                                |
| account         | Company name                                                                |
| deal_stage      | Sales pipeline stage (Prospecting > Engaging > Won / Lost)                  |
| engage_date     | Date in which the "Engaging" deal stage was initiated                       |
| close_date      | Date in which the deal was "Won" or "Lost"                                  |
| close_value     | Revenue from the deal                                                       |

---
### **Data Model**
I worked on identifying the relationships between the tables and came up with this diagram.

![data model.png](Visualizations/60518354-5616-4469-8f68-477934c5d9dd.png)

---

### **Business Goal**  
#### 1. How is each sales team performing compared to the rest?  
#### 2. Are any sales agents lagging behind?  
#### 3. Can you identify any quarter-over-quarter trends?  

---

### **KPIs**  
1. **Total Bookings**: The sum of all closed deals.  
   - In our dataset, it is the sum of the values in the `close_value` column.  
   - We will use this metric to measure the success of sales teams and sales agents.  
   - Which region has a high loss of deals?  

2. **Average Deal Size**: The average size (in dollars) of all won deals.  
   - In our dataset, it is the sum of the values in the `close_value` column for won deals divided by the number of deals.  
   - This metric will help us identify the type of customers and deals we should focus on.  

3. **Average Time to Close**: The average number of days it takes a member of the sales team to close a deal, from the prospect stage to a closed deal.  
   - We will calculate this metric based on the `engage_date`, as we don’t have the date when the Prospecting stage was initiated.  
   - We will use this metric to investigate how many days, on average, each sales team took to close a deal.  

4. **Win Rate**: The percentage of successful sales from created opportunities and/or new prospects over a specific period of time.  
   - It is calculated as the number of Closed-won deals divided by the total number of deals.  
   - We will use it to determine which sales agents are performing the best and which are lagging.  



This analysis is performed for deals closed between **March 1, 2017**, and **December 31, 2017**.  
### **Analysis Questions**  
- What is the total bookings for each sales team per region?
- What are the trends in win rate over time?
- Which region has a high loss of deals?
- What is the average time to close a deal per sales team?
- What is the total bookings for each sales agent?  
- What is the average time to close a deal per sales agent?
- Which sales agent has the top performance?    

## **Data Assessing**  
- For this step, we will use **Power Query**.  

#### **`Accounts` Table**  
- The `subsidiary_of` column has missing values, but we will keep it since we will not use it.  
- No duplicates rows

#### **`Products` Table**  
- There are no missing values.  
- No duplicate rows

#### **`Sales Teams` Table**  
- No missing values
- No duplicate rows

#### **`Sales Pipeline` Table**  
- There are 8,800 opportunities in our dataset.
- There are no duplicate rows
- There are missing values in the `account`, `engage_date`, `close_date`, and `close_value` columns. These missing values correspond to opportunities still in the engaging or prospecting stages.
- We will focus solely on evaluating performance based on closed deals, so we will filter the data to include only lost and won deals.
- If we lose a deal, the `close_value` is 0.



  
However, before we begin, we will use **Power Pivot** to establish relationships between the tables and calculate our KPIs.

## **Data Cleaning**
1. Filter the Data to Include Only Lost and Won Deals
2. Create a New Column for the Number of Days to Close a Deal. We calculate the days to close a deal by finding the difference between `close_date` and `engage_date`.


    - **Power Query Formula**
        ```
        = Table.AddColumn(#"Filtered Rows", "time to close", each Duration.Days([close_date] - [engage_date]))
        ```
3. Modify `GTXPro` in sales_pipeline table to `GTX Pro` as in product table so that the data is consistent

## **Exploratory Data Analysis**
- We sell products to **85 companies** across **10 sectors**.  
- Most of our customers have office locations in the **United States**.  
- The company sells **7 products**.  
- There are **35 sales agents**.  
- There are **6 sales teams**.  
- There are **3 regional offices**, each with **2 sales teams**.  
- Every sales manager manages a team of **6 sales agents**, except for **Dustin Brinkmann**, who manages a team of **5 sales agents**.

![image.png](Visualizations/200c72a4-c5d1-4c04-b77e-372ae4ac3a92.png)

									
![image.png](Visualizations/74c441cb-e90a-4705-8a8c-ba6fa079e154.png)

- The mean close value is **2,361**, and the median close value is **1,117**, indicating the presence of outliers that skew the distribution to the right.  
- **75%** of the opportunities have a close value of less than **5,000**.  
- **50%** of the opportunities have a close value of less than **1,117**.  
- The total bookings amount to **10,005,534**.  
- The mode is **54**, which is significantly smaller than the median and mean, suggesting that a large number of deals have a small close value.  

![image.png](Visualizations/72f92b18-fd68-4460-847e-afb9a8229580.png)
- The company won 63.15% of the opportunities but lost 36.85%, a significant loss rate requiring further investigation.

![image.png](Visualizations/718c282a-f67e-4954-a752-06fdc1d3713d.png)

![image.png](Visualizations/76c895e8-2433-4a30-ac8e-fd25c0692bd6.png)

## Drawing Conclusions
Now, we will address the main questions.

### What is the total bookings for each sales team per region?
![image.png](Visualizations/4874b1de-bb82-4d77-aad0-359a4d0eac7e.png)

- Every region has a sales team that outperforms the others. Since this pattern appears in every region, it’s possible that each team focuses on deals for specific products based on price. We need to investigate this more.
- The total bookings for **Melvin Marxen's sales team** are the largest, reflecting their ability to close a high number of deals.  
- **Rocco Neubert's sales team** has the highest average deal size, reflecting their ability to close riskier deals, even though they do not have the largest total bookings.

![image.png](Visualizations/c804903a-7555-4fa2-96bc-d798ffa48a8a.png)

- In each region, the team that generates higher revenue than the other tends to close more deals involving high-value products, while the other team tends to close more deals involving low-value products.  
- **Celia Rouche's sales team** is the only team that sold the **GTK 500**, the most expensive product. This is what drives their average deal size to a higher value.  
- **Dustin Brinkmann's sales team** has the lowest average deal size, as it appears they sell more low-value products than high-value products.  

### What are the trends in win rate over time?

![image.png](Visualizations/a125ef6a-5433-474b-acd9-997fd7b5624c.png)

- There is a noticeable monthly trend in the win rate, as it increases every two months across all regions. Specifically:  
  - It increases in **March** and decreases in **April** and **May**.  
  - It increases in **June** and decreases in **July** and **August**.  
  - It increases in **September** and decreases in **October** and **November**.  
  - It then increases again in **December**.


- We need to investigate further to determine the cause of these fluctuations. Is it due to seasonal trends, marketing campaigns, or other factors? Understanding the reasons behind the increase in win rate will help us replicate this success during the months when the win rate decreases.

#### What is the average time to close a deal per sales team?

![image.png](Visualizations/e2e9c8fa-0a0c-4148-b984-bd63a6679618.png)


- Dustin Brinkmann's team takes the longest time to close deals but has a lower win rate compared to other teams, such as Cara Losch's team and Summer Sewald's team, which perform above the trendline. This suggests that spending more time on deals does not necessarily translate into higher win rates for this team, indicating potential inefficiencies in their sales process.


- Melvin Marxen's team has a low win rate despite selling the largest number of products and generating the highest total bookings. Improving this team’s win rate could significantly drive more profit for the company, as they are already closing a high volume of deals.


- Across regional offices, teams that take more time to close deals tend to have a higher win rate. This suggests that spending additional time on deals may lead to better outcomes, but the relationship varies by team and region.

#### Which sales agent has the top performance?  


![image.png](Visualizations/4acb4fe0-034e-4270-93ee-82fa89dcb9a9.png)

Hayden Neloms is the sales agent with the highest win rate of 70.39%. He is managed by Celia Rouche in the West region.

Darcel Schlecht is the sales agent with the highest total bookings, amounting to $1,153,214. He is managed by Melvin Marxen in the Central region. His total bookings are significantly higher compared to those of the other sales agents.

Lajuana Vencill is the sales agent with the lowest win rate of 54.98%, which is significantly low. She is managed by Dustin Brinkmann in the Central region.
