## Overview
In this project, I'm going to analyze transactional data that has been gathered over 4 years. The main goal of this analysis is to create visual representations of the data to assess the performance over these years. The primary interest of the stakeholders is in analyzing the profit. Specifically, the focus will be on the analysis of products, customer locations (countries), and time trends to identify any patterns or trends.

## Data Gathering
The data is stored in an Excel file, so I downloaded it and imported it into my analysis file. The file contains six sheets: `DimCustomer`, `DimDate`, `DimGeography`, `DimProduct`, `DimSalesTerritory`, and `FactInternetSales`.

## Data Assessing & Cleaning  
##### Using **Power Query**

### `FactInternetSales` Table
- We do not need all the columns in the `FactInternetSales` table for our analysis. Therefore, we will retain only the following necessary columns:  
  - `ProductKey`, `OrderDateKey`, `DueDateKey`, `ShipDateKey`, `CustomerKey`, `SalesTerritoryKey`, `OrderQuantity`, `UnitPrice`, and `ProductStandardCost`.

- We calculated the revenue:  
  - A custom column named `Total Revenue` was created using the following formula:  
    ```powerquery
    = Table.AddColumn(#"Changed Type1", "Total Revenue", each [OrderQuantity] * [UnitPrice])
    ```

- We calculated the Cost of Goods Sold (COGs):  
  - A new column named `COGs` was created using the following formula:  
    ```powerquery
    = Table.AddColumn(#"Changed Type2", "COGs", each [OrderQuantity] * [ProductStandardCost])
    ```

- We calculated the total profit:  
  - A new column named `Total Profit` was created using the following formula:  
    ```powerquery
    = Table.AddColumn(#"Changed Type3", "Total Profit", each [Total Revenue] - [COGs])
    ```

---

### `DimSalesTerritory` Table
- Removed the row where `SalesTerritoryKey` equals 11 because it has no value.
- Removed the `SalesTerritoryImage` column because it contains only null values.

---

### `DimProduct` Table
- Selected only the following columns for use in our analysis:  
  - `ProductKey`, `EnglishProductName`, and `Color`.
- Replaced `NA` values in the `Color` column with `Unspecified`.

---

### `DimGeography` Table
- Selected only the following columns for use in our analysis:  
  - `GeographyKey`, `City`, `EnglishCountryRegionName`, and `SalesTerritoryKey`.

---

### `DimDate` Table
- Since we are rebuilding this table from scratch, we deleted all columns except `FullDateAlternateKey`.
- Created a new column for `Year` and filtered it to include only the years 2005 to 2008, as these are the years present in the dataset.
- Created new columns for:
  - Month number (`MonthNumber`).
  - Month name (`MonthName`) shortened to three characters (e.g., "Jan", "Feb").
- Created a day name column (`DayName`).
- Created a new column called `WeekType` that categorizes days as either "Weekend" or "Weekday".
- Created a new column for year quarters (`Quarter`) and added a `Q` prefix to each value (e.g., "Q1", "Q2").

---

### `DimCustomer` Table
- Created a new column called `Full Name` by merging the `FirstName` and `LastName` columns.
- Selected the following columns for analysis:  
  - `CustomerKey`, `GeographyKey`, `CustomerAlternateKey`, `Full Name`, `BirthDate`, and `Gender`.


```python

```
