# **Overview**

### **Context:**
The growth of supermarkets in most populated cities is increasing, and market competition is also high. The dataset represents historical sales data from a supermarket company, recorded across three different branches over three months.

#### **Stakeholder Request:**  

We've been analyzing our sales performance across the three branches and noticed that while revenue is fairly consistent, there may be underlying differences in customer behavior, product preferences, and shopping patterns. We want to understand what drives customer spending, how product lines perform across locations, and whether certain factors—such as payment methods, time of purchase, or customer type—impact sales. Additionally, we want insights into overall sales trends over the past three months to guide future business decisions.

#### **Key Business Questions:**  
1. Which branch generates the **highest and lowest revenue**?  
2. How do **product line sales** vary across branches?  
3. Does **customer type (Members vs. Normal)** affect sales differently at each branch?  
4. What are the **peak shopping hours** for each branch?
5. What are the **peak shopping days of the week** for each branch?
6. Are certain **payment methods** more popular at specific branches?  
7. Do **customer satisfaction ratings** differ by branch, and do they correlate with revenue?
8. What are the trends in revenue over the past 3 months?


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from matplotlib.colors import ListedColormap
import warnings
warnings.filterwarnings('ignore')

plt.style.use('tableau-colorblind10')  # Change style here


```

# Data Gathering

The dataset is available in Kaggle and you can download it from this link [here](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales). It consists of 17 columns and 1000 rows.

#### **Attribute Information:**

- **Invoice ID**: Computer-generated sales slip invoice identification number.  
- **Branch**: Branch of the supercenter (3 branches are available, identified as A, B, and C).  
- **City**: Location of the supercenters.  
- **Customer Type**: Type of customers, recorded as:
  - **Member**: Customers using a member card.  
  - **Normal**: Customers without a member card.  
- **Gender**: Gender of the customer.  
- **Product Line**: General item categorization groups:
  - Electronic accessories  
  - Fashion accessories  
  - Food and beverages  
  - Health and beauty  
  - Home and lifestyle  
  - Sports and travel  
- **Unit Price**: Price of each product in dollars ($).  
- **Quantity**: Number of products purchased by the customer.  
- **Tax**: 5% tax fee applied to customer purchases.  
- **Total**: Total price including tax.  
- **Date**: Date of purchase (Records available from January 2019 to March 2019).  
- **Time**: Purchase time (Between 10 AM and 9 PM).  
- **Payment**: Payment method used by the customer (Three methods available: Cash, Credit Card, and E-wallet).  
- **COGS**: Cost of goods sold.  
- **Gross Margin Percentage**: Gross margin percentage.  
- **Gross Income**: Gross income.  
- **Rating**: Customer satisfaction rating on their overall shopping experience (On a scale of 1 to 10).  


```python
df = pd.read_csv('./dataset/supermarket_sales - Sheet1.csv')
```

# Data Assessing


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Branch</th>
      <th>City</th>
      <th>Customer type</th>
      <th>Gender</th>
      <th>Product line</th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Tax 5%</th>
      <th>Total</th>
      <th>Date</th>
      <th>Time</th>
      <th>Payment</th>
      <th>cogs</th>
      <th>gross margin percentage</th>
      <th>gross income</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>750-67-8428</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Female</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7</td>
      <td>26.1415</td>
      <td>548.9715</td>
      <td>1/5/2019</td>
      <td>13:08</td>
      <td>Ewallet</td>
      <td>522.83</td>
      <td>4.761905</td>
      <td>26.1415</td>
      <td>9.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>226-31-3081</td>
      <td>C</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Electronic accessories</td>
      <td>15.28</td>
      <td>5</td>
      <td>3.8200</td>
      <td>80.2200</td>
      <td>3/8/2019</td>
      <td>10:29</td>
      <td>Cash</td>
      <td>76.40</td>
      <td>4.761905</td>
      <td>3.8200</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>631-41-3108</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>46.33</td>
      <td>7</td>
      <td>16.2155</td>
      <td>340.5255</td>
      <td>3/3/2019</td>
      <td>13:23</td>
      <td>Credit card</td>
      <td>324.31</td>
      <td>4.761905</td>
      <td>16.2155</td>
      <td>7.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>123-19-1176</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Male</td>
      <td>Health and beauty</td>
      <td>58.22</td>
      <td>8</td>
      <td>23.2880</td>
      <td>489.0480</td>
      <td>1/27/2019</td>
      <td>20:33</td>
      <td>Ewallet</td>
      <td>465.76</td>
      <td>4.761905</td>
      <td>23.2880</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>373-73-7910</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7</td>
      <td>30.2085</td>
      <td>634.3785</td>
      <td>2/8/2019</td>
      <td>10:37</td>
      <td>Ewallet</td>
      <td>604.17</td>
      <td>4.761905</td>
      <td>30.2085</td>
      <td>5.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Branch</th>
      <th>City</th>
      <th>Customer type</th>
      <th>Gender</th>
      <th>Product line</th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Tax 5%</th>
      <th>Total</th>
      <th>Date</th>
      <th>Time</th>
      <th>Payment</th>
      <th>cogs</th>
      <th>gross margin percentage</th>
      <th>gross income</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>995</th>
      <td>233-67-5758</td>
      <td>C</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Health and beauty</td>
      <td>40.35</td>
      <td>1</td>
      <td>2.0175</td>
      <td>42.3675</td>
      <td>1/29/2019</td>
      <td>13:46</td>
      <td>Ewallet</td>
      <td>40.35</td>
      <td>4.761905</td>
      <td>2.0175</td>
      <td>6.2</td>
    </tr>
    <tr>
      <th>996</th>
      <td>303-96-2227</td>
      <td>B</td>
      <td>Mandalay</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Home and lifestyle</td>
      <td>97.38</td>
      <td>10</td>
      <td>48.6900</td>
      <td>1022.4900</td>
      <td>3/2/2019</td>
      <td>17:16</td>
      <td>Ewallet</td>
      <td>973.80</td>
      <td>4.761905</td>
      <td>48.6900</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>997</th>
      <td>727-02-1313</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Male</td>
      <td>Food and beverages</td>
      <td>31.84</td>
      <td>1</td>
      <td>1.5920</td>
      <td>33.4320</td>
      <td>2/9/2019</td>
      <td>13:22</td>
      <td>Cash</td>
      <td>31.84</td>
      <td>4.761905</td>
      <td>1.5920</td>
      <td>7.7</td>
    </tr>
    <tr>
      <th>998</th>
      <td>347-56-2442</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>65.82</td>
      <td>1</td>
      <td>3.2910</td>
      <td>69.1110</td>
      <td>2/22/2019</td>
      <td>15:33</td>
      <td>Cash</td>
      <td>65.82</td>
      <td>4.761905</td>
      <td>3.2910</td>
      <td>4.1</td>
    </tr>
    <tr>
      <th>999</th>
      <td>849-09-3807</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Female</td>
      <td>Fashion accessories</td>
      <td>88.34</td>
      <td>7</td>
      <td>30.9190</td>
      <td>649.2990</td>
      <td>2/18/2019</td>
      <td>13:28</td>
      <td>Cash</td>
      <td>618.38</td>
      <td>4.761905</td>
      <td>30.9190</td>
      <td>6.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1000 entries, 0 to 999
    Data columns (total 17 columns):
     #   Column                   Non-Null Count  Dtype  
    ---  ------                   --------------  -----  
     0   Invoice ID               1000 non-null   object 
     1   Branch                   1000 non-null   object 
     2   City                     1000 non-null   object 
     3   Customer type            1000 non-null   object 
     4   Gender                   1000 non-null   object 
     5   Product line             1000 non-null   object 
     6   Unit price               1000 non-null   float64
     7   Quantity                 1000 non-null   int64  
     8   Tax 5%                   1000 non-null   float64
     9   Total                    1000 non-null   float64
     10  Date                     1000 non-null   object 
     11  Time                     1000 non-null   object 
     12  Payment                  1000 non-null   object 
     13  cogs                     1000 non-null   float64
     14  gross margin percentage  1000 non-null   float64
     15  gross income             1000 non-null   float64
     16  Rating                   1000 non-null   float64
    dtypes: float64(7), int64(1), object(9)
    memory usage: 132.9+ KB
    


```python
cat_cols = ['Branch', 'City', 'Customer type', 'Gender',
       'Product line', 'Payment']
for col in cat_cols:
    print(df[col].unique())
    print('-' * 40)
```

    ['A' 'C' 'B']
    ----------------------------------------
    ['Yangon' 'Naypyitaw' 'Mandalay']
    ----------------------------------------
    ['Member' 'Normal']
    ----------------------------------------
    ['Female' 'Male']
    ----------------------------------------
    ['Health and beauty' 'Electronic accessories' 'Home and lifestyle'
     'Sports and travel' 'Food and beverages' 'Fashion accessories']
    ----------------------------------------
    ['Ewallet' 'Cash' 'Credit card']
    ----------------------------------------
    


```python
df['gross margin percentage'].value_counts()
```




    gross margin percentage
    4.761905    1000
    Name: count, dtype: int64




```python
(100 * df['gross income'] / df['Total']).round(6).unique()
```




    array([4.761905])



- They have a fixed gross margin of approximately 4.8%.


```python
(df['gross income'] == df['Tax 5%']).all()
```




    True



- We found that they only make a profit from the 5% tax added to the total price. That explains why they have a fixed gross margin.


```python
# check that gross income is calculated correctly

((df.Total - df.cogs).round(4) == df['gross income']).all()
```




    True




```python
((df['gross income'] / df.Total) * 100).round(6)
```




    0      4.761905
    1      4.761905
    2      4.761905
    3      4.761905
    4      4.761905
             ...   
    995    4.761905
    996    4.761905
    997    4.761905
    998    4.761905
    999    4.761905
    Length: 1000, dtype: float64




```python
df.duplicated().sum()
```




    0




```python
# let's ensure that every city has a unique branch
df[['City', 'Branch']].drop_duplicates()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Branch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Yangon</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Naypyitaw</td>
      <td>C</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mandalay</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>



#### Data Assessment Conclusion:
- No missing values
- No duplicate rows
- No inconsistencies issues in categorical columns
- Measures are calculated correctly
- They have a fixed gross margin of approximately 4.8%
#### Data Quality Issues
- The `Date` and `Time` columns have an incorrect data type

# Data Cleaning


```python
df_clean = df.copy()
```

##### Change `Date` column data type from `object` to `datetime` using `pd.to_datetime`


```python
df_clean['Date'] = pd.to_datetime(df_clean['Date'])
```

##### Test


```python
df_clean['Date'].head()
```




    0   2019-01-05
    1   2019-03-08
    2   2019-03-03
    3   2019-01-27
    4   2019-02-08
    Name: Date, dtype: datetime64[ns]



##### Extract the hour from the `Time` column


```python
df_clean['hour'] = df_clean.Time.apply(lambda x: x.split(':')[0])
```

##### Test


```python
df_clean['hour'].value_counts()
```




    hour
    19    113
    13    103
    15    102
    10    101
    18     93
    11     90
    12     89
    14     83
    16     77
    20     75
    17     74
    Name: count, dtype: int64



##### Extract the day of the week from the Date column


```python
df_clean['day_of_week'] = df_clean.Date.dt.day_name().str[:3]
```

##### Test


```python
df_clean['day_of_week'].head()
```




    0    Sat
    1    Fri
    2    Sun
    3    Sun
    4    Fri
    Name: day_of_week, dtype: object



##### Rename `Total` to `Revenue`


```python
df_clean = df_clean.rename(columns={'Total': 'Revenue'})
```

##### Test


```python
df_clean.columns
```




    Index(['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender',
           'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Revenue', 'Date',
           'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income',
           'Rating', 'hour', 'day_of_week'],
          dtype='object')



##### Drop unnecessary column for analysis
- Every city has a branch, so we can drop either the `Branch` or `City` column since they contain redundant information.  
- The `gross margin percentage` is a fixed value for all orders. As mentioned earlier, the company only makes a profit from the 5% tax applied to each order's total price. Therefore, the `gross income` equals the `Tax 5%`, so I will drop the `Tax 5%` column and the `gross margin percentage`.  
- Since we have already extracted the `hour` from the `Time` column, we can drop it now.



```python
cols_to_drop = ['Branch', 'Tax 5%', 'Time', 'gross margin percentage']

df_clean = df_clean.drop(columns=cols_to_drop, axis=1)
```


```python
df_clean.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>City</th>
      <th>Customer type</th>
      <th>Gender</th>
      <th>Product line</th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Revenue</th>
      <th>Date</th>
      <th>Payment</th>
      <th>cogs</th>
      <th>gross income</th>
      <th>Rating</th>
      <th>hour</th>
      <th>day_of_week</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>750-67-8428</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Female</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7</td>
      <td>548.9715</td>
      <td>2019-01-05</td>
      <td>Ewallet</td>
      <td>522.83</td>
      <td>26.1415</td>
      <td>9.1</td>
      <td>13</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>226-31-3081</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Electronic accessories</td>
      <td>15.28</td>
      <td>5</td>
      <td>80.2200</td>
      <td>2019-03-08</td>
      <td>Cash</td>
      <td>76.40</td>
      <td>3.8200</td>
      <td>9.6</td>
      <td>10</td>
      <td>Fri</td>
    </tr>
    <tr>
      <th>2</th>
      <td>631-41-3108</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>46.33</td>
      <td>7</td>
      <td>340.5255</td>
      <td>2019-03-03</td>
      <td>Credit card</td>
      <td>324.31</td>
      <td>16.2155</td>
      <td>7.4</td>
      <td>13</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>3</th>
      <td>123-19-1176</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Male</td>
      <td>Health and beauty</td>
      <td>58.22</td>
      <td>8</td>
      <td>489.0480</td>
      <td>2019-01-27</td>
      <td>Ewallet</td>
      <td>465.76</td>
      <td>23.2880</td>
      <td>8.4</td>
      <td>20</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>4</th>
      <td>373-73-7910</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7</td>
      <td>634.3785</td>
      <td>2019-02-08</td>
      <td>Ewallet</td>
      <td>604.17</td>
      <td>30.2085</td>
      <td>5.3</td>
      <td>10</td>
      <td>Fri</td>
    </tr>
  </tbody>
</table>
</div>



# Exploratory Data Analysis


```python
df_clean.describe(include=np.number)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Revenue</th>
      <th>cogs</th>
      <th>gross income</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1000.000000</td>
      <td>1000.000000</td>
      <td>1000.000000</td>
      <td>1000.00000</td>
      <td>1000.000000</td>
      <td>1000.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>55.672130</td>
      <td>5.510000</td>
      <td>322.966749</td>
      <td>307.58738</td>
      <td>15.379369</td>
      <td>6.97270</td>
    </tr>
    <tr>
      <th>std</th>
      <td>26.494628</td>
      <td>2.923431</td>
      <td>245.885335</td>
      <td>234.17651</td>
      <td>11.708825</td>
      <td>1.71858</td>
    </tr>
    <tr>
      <th>min</th>
      <td>10.080000</td>
      <td>1.000000</td>
      <td>10.678500</td>
      <td>10.17000</td>
      <td>0.508500</td>
      <td>4.00000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>32.875000</td>
      <td>3.000000</td>
      <td>124.422375</td>
      <td>118.49750</td>
      <td>5.924875</td>
      <td>5.50000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>55.230000</td>
      <td>5.000000</td>
      <td>253.848000</td>
      <td>241.76000</td>
      <td>12.088000</td>
      <td>7.00000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>77.935000</td>
      <td>8.000000</td>
      <td>471.350250</td>
      <td>448.90500</td>
      <td>22.445250</td>
      <td>8.50000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>99.960000</td>
      <td>10.000000</td>
      <td>1042.650000</td>
      <td>993.00000</td>
      <td>49.650000</td>
      <td>10.00000</td>
    </tr>
  </tbody>
</table>
</div>



- The mean and median of the unit price are very close to each other. The cheapest product has a unit price of \\$10, while the most expensive one has a unit price of \\$100.  
- The highest order size is 10.  
- The mean revenue is larger than the median, which implies a right-skewed distribution and the presence of outliers.  
- The lowest rating a client has given is 4.


```python
sns.pairplot(df_clean)
plt.show()
```


    
![png](Presentations Images/output_43_0.png)
    


- We can see that the revenue is right-skewed, as expected, and most of the orders have revenue less than \\$500.
- There is no relationship between revenue and rating.
- Unit price, quantity, and rating have an approximately uniform distribution.

# Drawing Conclusions

#### Which branch generates the highest and lowest revenue?  


```python
df_clean.columns
```




    Index(['Invoice ID', 'City', 'Customer type', 'Gender', 'Product line',
           'Unit price', 'Quantity', 'Revenue', 'Date', 'Payment', 'cogs',
           'gross income', 'Rating', 'hour', 'day_of_week'],
          dtype='object')




```python
base_color = sns.color_palette()[0]
sec_color = sns.color_palette()[2]
```


```python
branch_revenue = df_clean.groupby('City')['Revenue'].sum().sort_values(ascending=False)
branch_orders = df_clean.City.value_counts()
```


```python
revenue_color =[base_color if v == max(branch_revenue) else sec_color for v in branch_revenue]
orders_color = [base_color if v == max(branch_orders) else sec_color for v in branch_orders]

revenue_color
```




    [(0.0, 0.4196078431372549, 0.6431372549019608),
     (0.6705882352941176, 0.6705882352941176, 0.6705882352941176),
     (0.6705882352941176, 0.6705882352941176, 0.6705882352941176)]




```python


plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.barplot(data=df_clean, x='City', y='Revenue', 
            order=branch_revenue.index,
            estimator='sum', palette=revenue_color)
plt.title('Total Revenue by Branch')
plt.ylabel('Total Revenue')

plt.subplot(1, 2, 2)
sns.countplot(data=df_clean, x='City', order=branch_orders.index, palette=orders_color)
plt.title('Total Number of Orders by Branch')
plt.ylabel('Total Number of Orders')

plt.savefig('Vis/1_total_revenue_by_branch')
plt.show()
```


    
![png](Presentations Images/output_51_0.png)
    


- The Naypyitaw branch shows slightly higher revenue than the other branches.  
- However, the overlapping confidence intervals suggest that this difference may not be statistically significant, meaning we cannot confidently generalize this trend beyond the observed data.  
- Although the Yangon and Mandalay branches sold slightly more orders than the Naypyitaw branch, Naypyitaw has higher revenue, indicating that the Naypyitaw branch may have sold more high-value orders or orders that have larger orders sizes.

#### How do product line sales vary across branches?  


```python
revenue_by_product_line = df_clean.groupby('Product line')['Revenue'].median().sort_values(ascending=False)
```


```python
product_color = {k:base_color if v in revenue_by_product_line[:2].values else sec_color for k, v in revenue_by_product_line.items()}
```


```python
plt.figure(figsize=(10, 5))
sns.pointplot(data=df_clean, x='Product line', y='Revenue', estimator='median',
              order=revenue_by_product_line.index,
              palette=product_color)
plt.title('How Revenue Varies Across Product Lines')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('Vis/2_revenue_by_product_line')
plt.show()
```


    
![png](Presentations Images/output_56_0.png)
    


- `Fashion accessories` has the lowest revenue while `Health and beauty` and `Sports and travel` achieve the highest.
- Additionally, there is an overlap between the confidence intervals so we don't have statistically significant evidence to generalize these differences beyond the observed data.


```python
sns.catplot(data=df_clean, x='City', kind='count', hue='Product line', aspect=2)
plt.title('Number of Orders by Product Line per Branch')
plt.show()
```


    
![png](Presentations Images/output_58_0.png)
    


`Home and Lifestyle` is the most ordered product line in Yangon. However, `Food and Beverages` and `Fashion Accessories` are the most ordered in Naypyitaw. In Mandalay, `Sports and Travel` and `Fashion Accessories` are the most ordered.


```python
sns.catplot(data=df_clean, x='City', y='Revenue', kind='bar', hue='Product line', aspect=2, 
            estimator='median',
            errorbar=None)
plt.title('Revenue by Product Line per Branch')
plt.show()
```


    
![png](Presentations Images/output_60_0.png)
    


- We can see that `Health and Beauty` has the highest revenue in Mandalay.  
- However, `Health and Beauty` and `Electronic Accessories` have the lowest revenue in Yangon.  
- Additionally, `Home and Lifestyle` has the lowest revenue in Naypyitaw.


```python
revenue_and_order_count_by_city_branch = df_clean.groupby(['City', 'Product line'], as_index=False)\
.agg(Median_Revenue=('Revenue', 'median'), Orders_Count=('Invoice ID', 'count'), Average_Quantity=('Quantity', 'mean'),
    Average_UnitPrice=('Unit price', 'mean'))
revenue_and_order_count_by_city_branch
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Product line</th>
      <th>Median_Revenue</th>
      <th>Orders_Count</th>
      <th>Average_Quantity</th>
      <th>Average_UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mandalay</td>
      <td>Electronic accessories</td>
      <td>225.0150</td>
      <td>55</td>
      <td>5.745455</td>
      <td>49.854182</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mandalay</td>
      <td>Fashion accessories</td>
      <td>185.7555</td>
      <td>62</td>
      <td>4.790323</td>
      <td>54.843871</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mandalay</td>
      <td>Food and beverages</td>
      <td>234.8010</td>
      <td>50</td>
      <td>5.400000</td>
      <td>55.540000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mandalay</td>
      <td>Health and beauty</td>
      <td>350.0700</td>
      <td>53</td>
      <td>6.037736</td>
      <td>58.185660</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mandalay</td>
      <td>Home and lifestyle</td>
      <td>262.5840</td>
      <td>50</td>
      <td>5.900000</td>
      <td>55.514000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Mandalay</td>
      <td>Sports and travel</td>
      <td>275.3100</td>
      <td>62</td>
      <td>5.193548</td>
      <td>59.678065</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Naypyitaw</td>
      <td>Electronic accessories</td>
      <td>272.5800</td>
      <td>55</td>
      <td>6.054545</td>
      <td>55.809455</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Naypyitaw</td>
      <td>Fashion accessories</td>
      <td>267.3405</td>
      <td>65</td>
      <td>5.261538</td>
      <td>59.736000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Naypyitaw</td>
      <td>Food and beverages</td>
      <td>292.5405</td>
      <td>66</td>
      <td>5.590909</td>
      <td>57.273030</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Naypyitaw</td>
      <td>Health and beauty</td>
      <td>275.6040</td>
      <td>52</td>
      <td>5.326923</td>
      <td>55.971346</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Naypyitaw</td>
      <td>Home and lifestyle</td>
      <td>206.7975</td>
      <td>45</td>
      <td>5.444444</td>
      <td>54.334222</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Naypyitaw</td>
      <td>Sports and travel</td>
      <td>266.0280</td>
      <td>45</td>
      <td>5.888889</td>
      <td>55.107333</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Yangon</td>
      <td>Electronic accessories</td>
      <td>207.0705</td>
      <td>60</td>
      <td>5.366667</td>
      <td>54.871167</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Yangon</td>
      <td>Fashion accessories</td>
      <td>277.6725</td>
      <td>51</td>
      <td>5.156863</td>
      <td>56.670392</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Yangon</td>
      <td>Food and beverages</td>
      <td>249.0705</td>
      <td>58</td>
      <td>5.396552</td>
      <td>54.974483</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Yangon</td>
      <td>Health and beauty</td>
      <td>217.1820</td>
      <td>47</td>
      <td>5.468085</td>
      <td>49.862340</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Yangon</td>
      <td>Home and lifestyle</td>
      <td>263.1300</td>
      <td>65</td>
      <td>5.707692</td>
      <td>55.845692</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Yangon</td>
      <td>Sports and travel</td>
      <td>271.2780</td>
      <td>59</td>
      <td>5.644068</td>
      <td>55.610339</td>
    </tr>
  </tbody>
</table>
</div>




```python
g = sns.relplot(x='Orders_Count', y='Median_Revenue', data=revenue_and_order_count_by_city_branch,
            kind='scatter', col='City', hue='Product line', size='Average_Quantity')

g.fig.suptitle('Median Revenue vs Orders Count by City and Product Line', fontsize=14, y=1.05)

plt.savefig('Vis/3_revenue_order_count_by_city_product_line')
plt.show()
```


    
![png](Presentations Images/output_63_0.png)
    


- In Mandalay, despite `Health and Beauty` not having the highest number of orders, it achieves the highest revenue among all categories in all cities. Additionally, the `Sports and Travel` category has higher revenue than `Fashion Accessories` despite having the same number of orders.  
- In Naypyitaw, all categories are performing well compared to other categories in other cities, except for the `Home and Lifestyle` category, which has low revenue and a low number of orders.  
- In Yangon, the `Electronic Accessories` category has a high number of orders but low revenue. Also, the `Health and Lifestyle` category has both low revenue and a low number of orders.

#### Does customer type (Members vs. Normal) affect sales differently at each branch? 


```python
df_clean.columns
```




    Index(['Invoice ID', 'City', 'Customer type', 'Gender', 'Product line',
           'Unit price', 'Quantity', 'Revenue', 'Date', 'Payment', 'cogs',
           'gross income', 'Rating', 'hour', 'day_of_week'],
          dtype='object')




```python
sns.barplot(x='Customer type', y='Revenue', data=df_clean, estimator='median')
plt.title('Revenue by Customer Type')
plt.xlabel('Customer Type')
plt.savefig('Vis/4_Revenue_by_customer')
plt.show()
```


    
![png](Presentations Images/output_67_0.png)
    


- We can see that customers who are members achieve slightly higher revenue than those who are not.


```python
revenue_and_order_count_by_city_customer= df_clean.groupby(['City', 'Customer type'], as_index=False)\
.agg(median_revenue=('Revenue', 'median'), orders_count=('Invoice ID', 'count'))
revenue_and_order_count_by_city_customer
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Customer type</th>
      <th>median_revenue</th>
      <th>orders_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mandalay</td>
      <td>Member</td>
      <td>258.6780</td>
      <td>165</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mandalay</td>
      <td>Normal</td>
      <td>231.2415</td>
      <td>167</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Naypyitaw</td>
      <td>Member</td>
      <td>270.2595</td>
      <td>169</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>277.7880</td>
      <td>159</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Yangon</td>
      <td>Member</td>
      <td>262.4580</td>
      <td>167</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Yangon</td>
      <td>Normal</td>
      <td>226.0650</td>
      <td>173</td>
    </tr>
  </tbody>
</table>
</div>




```python
g = sns.relplot(x='orders_count', y='median_revenue', data=revenue_and_order_count_by_city_customer,
            kind='scatter', col='City', hue='Customer type',
               legend=False)

for ax, city in zip(g.axes.flat, revenue_and_order_count_by_city_customer.City.unique()):
    ax.set_ylabel('Median Revenue')
    ax.set_xlabel('Orders Count')
    for i, point in revenue_and_order_count_by_city_customer.query("City == @city").iterrows():
        ax.annotate(
            text=point["Customer type"], 
            xy=(point["orders_count"], point["median_revenue"]),
            xytext=(5,5),  
            textcoords="offset points",
            fontsize=10,
            color="black"
        )
y_ticks = np.arange(0, 280 + 50, 50)
x_ticks = np.arange(0, 200 + 20, 20)

plt.yticks(y_ticks, y_ticks)
plt.xticks(x_ticks, x_ticks)
g.fig.suptitle('Median Revenue vs Orders Count by City and Customer Type', fontsize=14, y=1.05)



plt.savefig('Vis/5_revenue_order_count_by_city_customer')
plt.show()
```


    
![png](Presentations Images/output_70_0.png)
    


- In Mandalay and Yangon, members generate higher revenue than normal customers, but normal customers place more orders.  
- In Naypyitaw, revenue is very close between both groups, but member customers have more orders than normal customers.  
- Overall, regardless of the supermarket branch, member customers contribute more to revenue.

#### What are the peak shopping hours for each branch?  


```python
order_count_by_hour_and_branch = df_clean.groupby(['City'], as_index=False)['hour'].value_counts()
order_count_by_hour_and_branch = order_count_by_hour_and_branch.sort_values(by='hour')
```


```python
sns.lineplot(data=order_count_by_hour_and_branch, 
            x='hour', 
            y='count',
            hue='City')

plt.title('Orders Count trends over the Day per Branch')
plt.xlabel('Hour')
plt.ylabel('Orders Count')
plt.savefig('Vis/6_orders_count_by_hour')
plt.show()
```


    
![png](Presentations Images/output_74_0.png)
    


- The order count in the Mandalay branch significantly dropped at 16:00 and 17:00 before rising again, reaching its peak at 19:00.
- In Naypyitaw and Yangon, order counts fluctuate normally throughout the day and never drop below 20 or exceed 40 in any given hour.
- **Recommendation:**
    - We must analyze how Mandalay reached 50 orders at 19:00 and attempt to implement similar strategies in other branches.
    - Additionally, we need to investigate why the order counts drop significantly at 16:00 and 17:00.

#### What are the peak shopping days of the week for each branch?  
   - Create a count plot to show the distribution of the number of orders per day of the week per branch. 


```python
order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sns.catplot(data=df_clean, x='day_of_week', col='City', 
            order = order,
            kind='count')
plt.show()
```


    
![png](Presentations Images/output_77_0.png)
    


- The Yangon branch has the lowest number of orders on Wednesday and Thursday compared to other days.  
- The Naypyitaw branch has the lowest number of orders on Monday and Friday, while the highest number of orders occurs on Tuesday and Saturday.  
- The Mandalay branch has the lowest number of orders on Monday and Sunday, with the highest number of orders on Saturday.

#### Are certain payment methods more popular at specific branches? 


```python
sns.countplot(data=df_clean, x='Payment', hue='City')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('Orders Count per Payment Method by Branch')
plt.xlabel('')
plt.tight_layout()
plt.savefig('Vis/7_payment_method_per_branch')
plt.show()
```


    
![png](Presentations Images/output_80_0.png)
    


- E-wallets are used more in the Yangon branch, while cash is used more in the Naypyitaw branch, and credit cards are used more in the Mandalay branch.


```python
sns.countplot(data=df_clean, x='Payment', hue='Customer type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('Orders Count per Payment Method by Customer Type')
plt.xlabel('')
plt.tight_layout()
plt.savefig('Vis/8_orders_count_per_payment_by_customer')
plt.show()
```


    
![png](Presentations Images/output_82_0.png)
    


- Members use credit cards more than normal customers. On the other hand, normal customers use e-wallets and cash more than member customers.


```python
sns.countplot(data=df_clean, x='Gender', hue='Customer type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```


    
![png](Presentations Images/output_84_0.png)
    


#### Do customer satisfaction ratings differ by branch, and do they correlate with revenue?  
   - Create a violin plot to examine the distribution of ratings for each branch.  
   - Create a scatter plot between revenue and ratings by branch. 


```python
sns.relplot(x='Rating', y='Revenue', data=df_clean, hue='City')
plt.show()
```


    
![png](Presentations Images/output_86_0.png)
    


- There is no relationship between rating and revenue.


```python
low_rating_orders = df_clean.query('Rating < 6')
```


```python
plt.figure(figsize=(12, 5))
sns.countplot(data=low_rating_orders, x='Product line', hue='City')

plt.title('Number of Low-Rated Orders per Product Line by Branch')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('Vis/9_ratings_per_product_line_by_branch')
plt.show()
```


    
![png](Presentations Images/output_89_0.png)
    


- Most of the low-rated orders in the `Sports and travel` and `Fashion accessories` categories are in the Mandalay branch.  
- Most of the low-rated orders in `Electronic accessories` are in the Yangon and Naypyitaw branches.  
- Most of the low-rated orders in `Food and beverages` are in the Naypyitaw branch.  
- Most of the low-rated orders in `Home and Style` are in the Yangon and Mandalay branches.

#### What are the trends in revenue over the past three months?  
   - Create a line plot to identify any trends in revenue over the past three months.


```python
mean_revenue = df_clean.groupby('Date').Revenue.mean().sort_values()
highest_revenue = mean_revenue.tail(1)
lowest_revenue = mean_revenue.head(1)
```


```python
plt.figure(figsize=(12, 8))

ax = sns.lineplot(data=df_clean, x='Date', y='Revenue')

plt.xticks(rotation=15)
plt.title('Revenue Over time')

# Annotate Highest Revenue Point
ax.annotate(f'Highest Revenue \non {highest_revenue.index[0].strftime("%b %d, %Y")}', 
            (mdates.date2num(highest_revenue.index[0]), highest_revenue.iloc[0]), 
            color=sns.color_palette()[1],
            xytext=(55, 50), textcoords='offset points', 
            arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2", 
                            color=sns.color_palette()[1]))

# Annotate Lowest Revenue Point
ax.annotate(f'Lowest Revenue \non {lowest_revenue.index[0].strftime("%b %d, %Y")}', 
            (mdates.date2num(lowest_revenue.index[0]), lowest_revenue.iloc[0]), 
            color=sns.color_palette()[2],
            xytext=(55, -25), textcoords='offset points', 
            arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2", 
                            color=sns.color_palette()[2]))
plt.tight_layout()
plt.savefig('Vis/10_revenue_over_time')
plt.show()
```


    
![png](Presentations Images/output_93_0.png)
    


- There are significant fluctuations in revenue, and interestingly, we achieved both the highest and lowest revenue in February.


```python
df_clean = df_clean.sort_values(by='Date')
df_clean['mm_Revenue'] = df_clean.Revenue.rolling(window=14).mean()
df_clean = df_clean.dropna()
```


```python
plt.figure(figsize=(12, 5))
ax = sns.lineplot(data=df_clean, x='Date', y='mm_Revenue', estimator='mean')

plt.xticks(rotation=15)
plt.title('14-Day Moving Average of Revenue Over time')
plt.tight_layout()
plt.savefig('Vis/11_ma_revenue_over_time')
```


    
![png](Presentations Images/output_96_0.png)
    


- In general, We can say that there is a sudden increase in revenue at the start or the middle of each month.

Let's look at the orders that generate high revenue.


```python
# Calculating Q1 and Q3
Q1 = df_clean['Revenue'].quantile(0.25)
Q3 = df_clean['Revenue'].quantile(0.75)

# Calculating IQR
IQR = Q3 - Q1
upper_limit = Q3 + IQR * 1.5
high_revenue_orders = df_clean[df_clean['Revenue'] > upper_limit]
high_revenue_orders
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>City</th>
      <th>Customer type</th>
      <th>Gender</th>
      <th>Product line</th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Revenue</th>
      <th>Date</th>
      <th>Payment</th>
      <th>cogs</th>
      <th>gross income</th>
      <th>Rating</th>
      <th>hour</th>
      <th>day_of_week</th>
      <th>mm_Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>357</th>
      <td>554-42-2417</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Sports and travel</td>
      <td>95.44</td>
      <td>10</td>
      <td>1002.120</td>
      <td>2019-01-09</td>
      <td>Cash</td>
      <td>954.4</td>
      <td>47.720</td>
      <td>5.2</td>
      <td>13</td>
      <td>Wed</td>
      <td>312.19875</td>
    </tr>
    <tr>
      <th>699</th>
      <td>751-41-9720</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>97.50</td>
      <td>10</td>
      <td>1023.750</td>
      <td>2019-01-12</td>
      <td>Ewallet</td>
      <td>975.0</td>
      <td>48.750</td>
      <td>8.0</td>
      <td>16</td>
      <td>Sat</td>
      <td>418.43625</td>
    </tr>
    <tr>
      <th>792</th>
      <td>744-16-7898</td>
      <td>Mandalay</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Home and lifestyle</td>
      <td>97.37</td>
      <td>10</td>
      <td>1022.385</td>
      <td>2019-01-15</td>
      <td>Credit card</td>
      <td>973.7</td>
      <td>48.685</td>
      <td>4.9</td>
      <td>13</td>
      <td>Tue</td>
      <td>392.64075</td>
    </tr>
    <tr>
      <th>166</th>
      <td>234-65-2137</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>95.58</td>
      <td>10</td>
      <td>1003.590</td>
      <td>2019-01-16</td>
      <td>Cash</td>
      <td>955.8</td>
      <td>47.790</td>
      <td>4.8</td>
      <td>13</td>
      <td>Wed</td>
      <td>501.29925</td>
    </tr>
    <tr>
      <th>557</th>
      <td>283-26-5248</td>
      <td>Naypyitaw</td>
      <td>Member</td>
      <td>Female</td>
      <td>Food and beverages</td>
      <td>98.52</td>
      <td>10</td>
      <td>1034.460</td>
      <td>2019-01-30</td>
      <td>Ewallet</td>
      <td>985.2</td>
      <td>49.260</td>
      <td>4.5</td>
      <td>20</td>
      <td>Wed</td>
      <td>360.98400</td>
    </tr>
    <tr>
      <th>167</th>
      <td>687-47-8271</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Fashion accessories</td>
      <td>98.98</td>
      <td>10</td>
      <td>1039.290</td>
      <td>2019-02-08</td>
      <td>Credit card</td>
      <td>989.8</td>
      <td>49.490</td>
      <td>8.7</td>
      <td>16</td>
      <td>Fri</td>
      <td>390.45375</td>
    </tr>
    <tr>
      <th>422</th>
      <td>271-88-8734</td>
      <td>Naypyitaw</td>
      <td>Member</td>
      <td>Female</td>
      <td>Fashion accessories</td>
      <td>97.21</td>
      <td>10</td>
      <td>1020.705</td>
      <td>2019-02-08</td>
      <td>Credit card</td>
      <td>972.1</td>
      <td>48.605</td>
      <td>8.7</td>
      <td>13</td>
      <td>Fri</td>
      <td>426.19275</td>
    </tr>
    <tr>
      <th>350</th>
      <td>860-79-0874</td>
      <td>Naypyitaw</td>
      <td>Member</td>
      <td>Female</td>
      <td>Fashion accessories</td>
      <td>99.30</td>
      <td>10</td>
      <td>1042.650</td>
      <td>2019-02-15</td>
      <td>Credit card</td>
      <td>993.0</td>
      <td>49.650</td>
      <td>6.6</td>
      <td>14</td>
      <td>Fri</td>
      <td>372.50925</td>
    </tr>
    <tr>
      <th>996</th>
      <td>303-96-2227</td>
      <td>Mandalay</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Home and lifestyle</td>
      <td>97.38</td>
      <td>10</td>
      <td>1022.490</td>
      <td>2019-03-02</td>
      <td>Ewallet</td>
      <td>973.8</td>
      <td>48.690</td>
      <td>4.4</td>
      <td>17</td>
      <td>Sat</td>
      <td>310.92150</td>
    </tr>
  </tbody>
</table>
</div>



# Communicating Results

![image.png](Presentations Images/f8354de1-705c-4fb9-bf6e-5c953742dcef.png)

![image.png](Presentations Images/43c693e9-5dd0-48e1-8eb6-074434fbe5d3.png)

![image.png](Presentations Images/d6baa0b3-ad1f-4eed-bf36-d2da708ec3a5.png)

![image.png](Presentations Images/f49caac3-d3d0-4bd2-84ed-6df92a8226ab.png)

![image.png](Presentations Images/6d124b30-5086-42cf-a08f-62ec004f30fd.png)

![image.png](Presentations Images/10136b73-61ae-46d6-b975-3f329c49ff64.png)

![image.png](Presentations Images/cf07202e-c225-4aee-82ab-5706fc83229d.png)

![image.png](Presentations Images/ee532bd2-1048-41e4-9ca6-c393513f1a8e.png)

![image.png](Presentations Images/41595b20-d413-4428-8812-870b449e05d6.png)

![image.png](Presentations Images/38b77e6c-5397-443f-b500-c5bc8b5cc6dc.png)

![image.png](Presentations Images/a883c4f6-cde8-4016-aa24-54c3a9e23884.png)

![image.png](Presentations Images/c7039423-1db6-40d2-85d8-ae61629c67ea.png)

![image.png](Presentations Images/2118af5b-1e1d-4f70-b894-7c6b3a4cdde0.png)

![image.png](Presentations Images/811fd70f-8f84-4946-b18e-01f32241a2ba.png)

![image.png](Presentations Images/81811b27-25e4-49dd-a201-76fb245bbf69.png)

![image.png](Presentations Images/301b76ef-d80c-494a-b697-a64bf6e6a7c6.png)

![image.png](Presentations Images/001774ea-0c0a-4262-8679-3b942009f5f4.png)

![image.png](Presentations Images/27a41394-d92f-4c5e-854f-18fea6b86b7d.png)

![image.png](Presentations Images/6c77a3a0-f97f-458d-b04d-48bb3aab0a2f.png)

![image.png](Presentations Images/d1f618e0-387e-4d54-a304-5b5eb3f090fb.png)

![image.png](Presentations Images/a6cc2be0-e56d-49fd-94dc-0d2947dff0de.png)

![image.png](Presentations Images/1ca21732-99a9-4d4f-8cee-54663b7b7607.png)

![image.png](Presentations Images/a16bd5d7-c863-41e6-a2b0-32f989338d81.png)

![image.png](Presentations Images/bd9c900c-dd23-4f31-bb21-c99a8cb0498d.png)

![image.png](Presentations Images/4bd171db-abfb-44b1-9f15-98c858f0ee26.png)

![image.png](Presentations Images/428e094e-4080-4f44-af72-e0288da5f096.png)

![image.png](Presentations Images/f928a45f-75a7-4ed1-82bd-38a69fc709f6.png)

![image.png](Presentations Images/ba796dec-9aea-49d1-92aa-998694176c0f.png)

![image.png](Presentations Images/7cbe72ca-3a40-4f17-8d19-d33c953c5146.png)

![image.png](Presentations Images/1755280a-6dce-4218-93dc-002a0fb5f424.png)

![image.png](Presentations Images/36ea165f-2c5a-40f1-8505-c2b4e42b16ef.png)

![image.png](Presentations Images/38847191-8d65-4f99-8b1d-9915fecabc8e.png)

![image.png](Presentations Images/56244f31-e1d9-4972-be1f-e5434f9857f4.png)

# Limitations
- I have only three months of data, so I can't reliably identify trends over time.  
- I don't have information about individual customers. For example, there is no unique identifier to track customer behavior, making it difficult to analyze customer churn and repeat purchase rates.
- I only have data about categories and not individual products, so I can't analyze the data at the product level.
