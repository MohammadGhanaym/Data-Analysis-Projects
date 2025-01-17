# Project: Movies Data Analysis 
## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

<a id='intro'></a>
## Introduction

>In this project, we'll be analyzing Movies data.
In particular, we'll be interested in knowing which genres are most popular from year to year? What kinds of properties are associated with movies that have high revenues? We will dig into this data to answer these questions.
This data set contains information about 10866 movies, including user ratings and revenue

**columns in this data set:**
- id
- imdb_id
- popularity
- budget
- revenue
- original_title
- cast
- homepage
- director
- tagline
- keywords
- overview
- runtime
- genres
- production_companies
- release_date
- vote_count
- vote_average
- release_year
- budget_adj
- revenue_adj
### Questions to answer
1. Which genre has the highest number of movies?
2. Which year has the highest number of moveis?
3. What is the relation between number of years and movies?
4. Which production company released the most number movies over the years?
5. How long time do movies take on average?
6. What is the relationship between popularity and vote count?
7. Does a bigger film production budget result in more revenue and popularity?
8. What is the status of movies rating over the years?
9. Which genres are most popular from year to year?
10. What kinds of properties are associated with movies that have high revenues?


```python
import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
%matplotlib inline
```

<a id='wrangling'></a>
## Data Wrangling

### General Properties


```python
fileName = 'tmdb-movies.csv'

# Checking that the file is in the same directory.
if not os.path.isfile(fileName):
    print("File not found. Check the path of the file and filename")

df = pd.read_csv(fileName)
```


```python
# To show all columns
pd.pandas.set_option('display.max_columns', None)
```


```python
# Taking a quick look at the data.
df.head(2)
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
      <th>id</th>
      <th>imdb_id</th>
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>cast</th>
      <th>homepage</th>
      <th>director</th>
      <th>tagline</th>
      <th>keywords</th>
      <th>overview</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>tt0369610</td>
      <td>32.985763</td>
      <td>150000000</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>http://www.jurassicworld.com/</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>monster|dna|tyrannosaurus rex|velociraptor|island</td>
      <td>Twenty-two years after the events of Jurassic ...</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>6/9/15</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>tt1392190</td>
      <td>28.419936</td>
      <td>150000000</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>http://www.madmaxmovie.com/</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>future|chase|post-apocalyptic|dystopia|australia</td>
      <td>An apocalyptic story set in the furthest reach...</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Village Roadshow Pictures|Kennedy Miller Produ...</td>
      <td>5/13/15</td>
      <td>6185</td>
      <td>7.1</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>3.481613e+08</td>
    </tr>
  </tbody>
</table>
</div>



### Assessing Data


```python
# looking deep at the properties of data
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10866 entries, 0 to 10865
    Data columns (total 21 columns):
     #   Column                Non-Null Count  Dtype  
    ---  ------                --------------  -----  
     0   id                    10866 non-null  int64  
     1   imdb_id               10856 non-null  object 
     2   popularity            10866 non-null  float64
     3   budget                10866 non-null  int64  
     4   revenue               10866 non-null  int64  
     5   original_title        10866 non-null  object 
     6   cast                  10790 non-null  object 
     7   homepage              2936 non-null   object 
     8   director              10822 non-null  object 
     9   tagline               8042 non-null   object 
     10  keywords              9373 non-null   object 
     11  overview              10862 non-null  object 
     12  runtime               10866 non-null  int64  
     13  genres                10843 non-null  object 
     14  production_companies  9836 non-null   object 
     15  release_date          10866 non-null  object 
     16  vote_count            10866 non-null  int64  
     17  vote_average          10866 non-null  float64
     18  release_year          10866 non-null  int64  
     19  budget_adj            10866 non-null  float64
     20  revenue_adj           10866 non-null  float64
    dtypes: float64(4), int64(6), object(11)
    memory usage: 1.7+ MB
    


```python
# columns that contain nan values
df.isnull().sum().sort_values(ascending = False)[:9]
```




    homepage                7930
    tagline                 2824
    keywords                1493
    production_companies    1030
    cast                      76
    director                  44
    genres                    23
    imdb_id                   10
    overview                   4
    dtype: int64



#### What I got from the previous cells:
- This dataset contains 10866 rows, and 21 columns.
- Columns that contain nan values: homepage, tagline, keywords, production_companies, cast, director, genres, imdb_id, and overview column.
- release_time column datatype needs to be changed to DateTime.
- id and imdb_id are unuseful columns, so they can be omitted.
- homepage also need to be drop since it has too much missing value.


```python
df.describe()
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
      <th>id</th>
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>runtime</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>1.086600e+04</td>
      <td>1.086600e+04</td>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>1.086600e+04</td>
      <td>1.086600e+04</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>66064.177434</td>
      <td>0.646441</td>
      <td>1.462570e+07</td>
      <td>3.982332e+07</td>
      <td>102.070863</td>
      <td>217.389748</td>
      <td>5.974922</td>
      <td>2001.322658</td>
      <td>1.755104e+07</td>
      <td>5.136436e+07</td>
    </tr>
    <tr>
      <th>std</th>
      <td>92130.136561</td>
      <td>1.000185</td>
      <td>3.091321e+07</td>
      <td>1.170035e+08</td>
      <td>31.381405</td>
      <td>575.619058</td>
      <td>0.935142</td>
      <td>12.812941</td>
      <td>3.430616e+07</td>
      <td>1.446325e+08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>5.000000</td>
      <td>0.000065</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>10.000000</td>
      <td>1.500000</td>
      <td>1960.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>10596.250000</td>
      <td>0.207583</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>90.000000</td>
      <td>17.000000</td>
      <td>5.400000</td>
      <td>1995.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20669.000000</td>
      <td>0.383856</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>99.000000</td>
      <td>38.000000</td>
      <td>6.000000</td>
      <td>2006.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>75610.000000</td>
      <td>0.713817</td>
      <td>1.500000e+07</td>
      <td>2.400000e+07</td>
      <td>111.000000</td>
      <td>145.750000</td>
      <td>6.600000</td>
      <td>2011.000000</td>
      <td>2.085325e+07</td>
      <td>3.369710e+07</td>
    </tr>
    <tr>
      <th>max</th>
      <td>417859.000000</td>
      <td>32.985763</td>
      <td>4.250000e+08</td>
      <td>2.781506e+09</td>
      <td>900.000000</td>
      <td>9767.000000</td>
      <td>9.200000</td>
      <td>2015.000000</td>
      <td>4.250000e+08</td>
      <td>2.827124e+09</td>
    </tr>
  </tbody>
</table>
</div>



Some basic statistics about data like mean, standard deviation, minimum, and maximum numbers.


```python
# checking if there is duplicted rows
df.duplicated().sum()
```




    1



There is a duplicated row.


```python
df.nunique()
```




    id                      10865
    imdb_id                 10855
    popularity              10814
    budget                    557
    revenue                  4702
    original_title          10571
    cast                    10719
    homepage                 2896
    director                 5067
    tagline                  7997
    keywords                 8804
    overview                10847
    runtime                   247
    genres                   2039
    production_companies     7445
    release_date             5909
    vote_count               1289
    vote_average               72
    release_year               56
    budget_adj               2614
    revenue_adj              4840
    dtype: int64



Number of unique values in the dateset

### Data Cleaning 
#### Tasks List
- [X] Dropping nan values in columns that we referred to in the previous cell.
- [X] Changing the data type of release_date column to datetime.
- [X] Dropping unuseful columns like id and imdb_id columns.
- [X] Dropping duplicated rows.


```python
# Defining a copy of the original dataset to avoid damaging the dataset if you do something wrong while cleaning.
df_cleaning = df.copy()
```


```python
# drop useless columns
to_drop = ['homepage', 'id', 'imdb_id', 'cast', 'tagline', 'overview', 'keywords']
df_cleaning.drop(columns = to_drop, inplace=True)
```


```python
# Replace all values of 0 with NAN
df_cleaning = df_cleaning.replace(0, np.nan)
```


```python
# looking at columns that contain nan values again.
df_cleaning.isnull().sum().sort_values(ascending = False)[:9]
```




    revenue_adj             6016
    revenue                 6016
    budget_adj              5696
    budget                  5696
    production_companies    1030
    director                  44
    runtime                   31
    genres                    23
    release_year               0
    dtype: int64




```python
# check that the columns have been dropped.
df_cleaning.columns
```




    Index(['popularity', 'budget', 'revenue', 'original_title', 'director',
           'runtime', 'genres', 'production_companies', 'release_date',
           'vote_count', 'vote_average', 'release_year', 'budget_adj',
           'revenue_adj'],
          dtype='object')




```python
# looking at the data to know its type in each column.
df_cleaning.head(1)
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
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>director</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.985763</td>
      <td>150000000.0</td>
      <td>1.513529e+09</td>
      <td>Jurassic World</td>
      <td>Colin Trevorrow</td>
      <td>124.0</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>6/9/15</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
    </tr>
  </tbody>
</table>
</div>




```python
# drop nan values
df_cleaning.dropna(inplace=True)
```


```python
# Making sure there are no missing values.
df_cleaning.isna().sum().sum()
```




    0




```python
# Changing release_date column data type
df_cleaning.release_date = pd.to_datetime(df_cleaning.release_date)
```


```python
# check release_date column data type
df_cleaning.dtypes
```




    popularity                     float64
    budget                         float64
    revenue                        float64
    original_title                  object
    director                        object
    runtime                        float64
    genres                          object
    production_companies            object
    release_date            datetime64[ns]
    vote_count                       int64
    vote_average                   float64
    release_year                     int64
    budget_adj                     float64
    revenue_adj                    float64
    dtype: object




```python
# drop duplicated rows
df_cleaning.drop_duplicates(inplace=True)
```


```python
# check duplicated rows
df_cleaning.duplicated().sum()
```




    0




```python
# Copy data again after cleaning
df = df_cleaning.copy()
```


```python
# check properties of data again
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 3807 entries, 0 to 10848
    Data columns (total 14 columns):
     #   Column                Non-Null Count  Dtype         
    ---  ------                --------------  -----         
     0   popularity            3807 non-null   float64       
     1   budget                3807 non-null   float64       
     2   revenue               3807 non-null   float64       
     3   original_title        3807 non-null   object        
     4   director              3807 non-null   object        
     5   runtime               3807 non-null   float64       
     6   genres                3807 non-null   object        
     7   production_companies  3807 non-null   object        
     8   release_date          3807 non-null   datetime64[ns]
     9   vote_count            3807 non-null   int64         
     10  vote_average          3807 non-null   float64       
     11  release_year          3807 non-null   int64         
     12  budget_adj            3807 non-null   float64       
     13  revenue_adj           3807 non-null   float64       
    dtypes: datetime64[ns](1), float64(7), int64(2), object(4)
    memory usage: 446.1+ KB
    

<a id='eda'></a>
## Exploratory Data Analysis
### 1.Which genre has the highest number of movies?


```python
df.genres.value_counts()[:10]
```




    Drama                   243
    Comedy                  230
    Drama|Romance           106
    Comedy|Romance          103
    Comedy|Drama|Romance     87
    Comedy|Drama             85
    Horror|Thriller          80
    Horror                   57
    Drama|Thriller           47
    Action|Thriller          39
    Name: genres, dtype: int64



Most of the movies in this dataset are comedy and drama movies. 


```python
# Taking a count of some values and plot a pie chart that represents the proportions of each item in this variable.
def pie_plot(x, labels, autopct, title=None):
    plt.figure(figsize=(8, 8))
    plt.pie(x, labels=labels, autopct=autopct)
    plt.title(title)
    plt.show()
```


```python
genres_count = df.genres.value_counts().values[:10]
labels = df.genres.value_counts().index[:10]
# pie chart of these genres number
pie_plot(genres_count, labels=labels, autopct='%.2f', title='Proportions of Movies Number')
```


    
![png](Visualizations/Visualizations/Visualizations/output_36_0.png)
    


### 2.Which year has the highest number of moveis?


```python
df.release_year.value_counts()[:10]
```




    2011    196
    2013    179
    2010    177
    2009    170
    2006    168
    2014    165
    2008    161
    2015    160
    2007    160
    2005    159
    Name: release_year, dtype: int64



Most of the movies in this dataset are released in 2011.


```python
years_count = df.release_year.value_counts().values[:10]
labels = df.release_year.value_counts().index[:10]
# pie chart of these years number
pie_plot(years_count, labels=labels, autopct='%.2f', title='Proportions of Years Number')
```


    
![png](Visualizations/Visualizations/Visualizations/output_40_0.png)
    


### 3.What is the relation between number of years and movies?


```python
# count the number of movies in each year then sort the result
movie_count_year = df['release_year'].value_counts().sort_index()
num_year = df.release_year.value_counts()
```


```python
movie_count_year.plot(kind= 'barh', figsize = (5, 20))
plt.title('Number of Movies Per Year')
plt.xlabel('Number of Movies')
plt.ylabel('Years')
plt.show()
```


    
![png](Visualizations/Visualizations/Visualizations/output_43_0.png)
    


The number of movies increases over years.

**Which year released highest number of movies?**

From the plot in 2011 over 175 movies has been released.

### 4.Which production company released the most number movies over the years?


```python
df.production_companies.value_counts()[:10]
```




    Paramount Pictures                        77
    Universal Pictures                        57
    Columbia Pictures                         39
    New Line Cinema                           38
    Warner Bros.                              33
    Metro-Goldwyn-Mayer (MGM)                 26
    Touchstone Pictures                       24
    Twentieth Century Fox Film Corporation    23
    20th Century Fox                          22
    Walt Disney Pictures                      22
    Name: production_companies, dtype: int64



Paramount Pictures company has released the most number of movies.


```python
company_count = df.production_companies.value_counts().values[:10]
labels = df.production_companies.value_counts().index[:10]
# pie chart of proportions of these companyies 
pie_plot(years_count, labels=labels, autopct= '%.2f', title= 'Proportions of Companies Number')
```


    
![png](Visualizations/Visualizations/Visualizations/output_49_0.png)
    


### 5.How long time do movies take on average?


```python
runtime_mean = df.runtime.mean()
print(runtime_mean)
```

    109.35093249277647
    


```python
# see some basic statistics for runtime column
df.runtime.describe()
```




    count    3807.000000
    mean      109.350932
    std        19.845761
    min        15.000000
    25%        96.000000
    50%       106.000000
    75%       119.000000
    max       338.000000
    Name: runtime, dtype: float64




```python
# histrogram for runtime and the number of movies

# figure size
plt.figure(figsize=(8,5))

# plot relationship between runtime and number of movies
plt.hist(df.runtime)

# histogram name
plt.title('Runtime of All Movies')

# x-axis name
plt.xlabel('Runtime')

# y-axis name
plt.ylabel('Number of Movies')
# show the histogram
plt.show()
```


    
![png](Visualizations/Visualizations/Visualizations/output_53_0.png)
    


These movies take 109.35 minute on average.

### 6.What is the relationship between popularity and vote count?


```python
def scatter_plot(x, y, color=None, title=None, xlabel=None, ylabel=None):
    # figure size
    plt.figure(figsize=(8, 5))
    
    # draw scatter plot to see the relationship between two variables
    plt.scatter(x, y, color=color)
    
    # plot title
    plt.title(title)
    
    # x-axis name
    plt.xlabel(xlabel)
    
    # y-axis name
    plt.ylabel(ylabel)
    plt.show()
```


```python
# Draw scatter plot to see the relationship between movies popularity and vote count.
scatter_plot(df.popularity, df.vote_count, title= 'The Relationship Between Movies Popularity and Vote Count',
            xlabel=  'Popularity', ylabel= 'Vote Count')
```


    
![png](Visualizations/Visualizations/Visualizations/output_57_0.png)
    


This makes sense since the increase in vote count causes an increase in popularity.

### 7.Does a bigger film production budget result in more revenue and popularity?


```python
# Draw scatter plot between budget and revenue
scatter_plot(df.budget, df.revenue, color= 'r', title= 'Revenue VS Budget', xlabel= 'Budget', ylabel= 'Revenue'  )
```


    
![png](Visualizations/Visualizations/Visualizations/output_60_0.png)
    



```python
# draw scatter plot between budget and popularity
scatter_plot(df.budget, df.popularity, color='y', title='Popularity VS Budget', xlabel='Budget', ylabel='popularity')
```


    
![png](Visualizations/Visualizations/Visualizations/output_61_0.png)
    


The two graphs are positively correlated, and that means the more budget is, the more popularity and revenue are.


### 8. What is the status of movies rating over the years?

We will use to columns the release year column and vote_average column

I will use `groupby` to get the mean of vote_average for each year


```python
avg_rating_year = df.groupby('release_year')['vote_average'].mean()
```


```python
# plot the relationship between release year and vote average
avg_rating_year.plot(kind='line', title = 'Average Rating VS Years', figsize=(8, 5))
plt.xlabel('Years')
plt.ylabel('Average Rating')
plt.show()
```


    
![png](Visualizations/Visualizations/Visualizations/output_66_0.png)
    


- **The average rating of movies is getting worse over the years, which means the old movies get high ratings than the new ones.**

### 9.Which genres are most popular from year to year?

I want to split the years into intervals and get the most popular genre in this interval. I will use `cut` to split years into intervals.


```python
year_levels = df.release_year.describe()[3:]

bin_edges = year_levels.tolist()
bin_edges = [int(year) for year in bin_edges]
bin_edges
```




    [1960, 1995, 2004, 2010, 2015]




```python
# Labels for the four years interval 
bin_names = ['1960:1995', '1995:2004', '2004:2010', '2010:2015']
```


```python
df['years_intervals'] = pd.cut(df['release_year'], bins=bin_edges, labels=bin_names)
```


```python
df.head(1)
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
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>director</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
      <th>years_intervals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.985763</td>
      <td>150000000.0</td>
      <td>1.513529e+09</td>
      <td>Jurassic World</td>
      <td>Colin Trevorrow</td>
      <td>124.0</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>2015-06-09</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
      <td>2010:2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().sum().sum()
```




    5




```python
df.dropna(inplace=True)
```


```python
df.isnull().sum().sum()
```




    0



Now, I will use `groupby` to get the most popular genres in each interval.


```python
count_genres_interval = df.groupby(['years_intervals', 'genres'] , as_index= False)['popularity'].mean()
```


```python
count_genres_interval.isnull().sum()
```




    years_intervals       0
    genres                0
    popularity         2555
    dtype: int64




```python
# We get nan values since there is genres that don't exist in all intervals.
count_genres_interval.dropna(inplace= True)
```


```python
most_popular_genres = []
max_popularity = []
intervals = df.years_intervals.unique()
for interval in intervals:
    filter_by_interval = count_genres_interval.loc[count_genres_interval.years_intervals == interval]
    most_popular_genres.append(filter_by_interval.genres[filter_by_interval.popularity.idxmax()])
    max_popularity.append(filter_by_interval.popularity.max())
```

Here we get the most popular genres and their popularity value.


```python
plt.figure(figsize=(8, 5))
color=['r', 'b', 'y', 'g']
for index in range(len(most_popular_genres)):
    plt.bar(x= df.years_intervals.unique()[index], height= max_popularity[index],
        color=color[index], label=most_popular_genres[index])
    plt.xticks(df.years_intervals.unique())
    plt.legend(loc='best')
plt.xlabel('Intervals')
plt.ylabel('Max popularity')
plt.title('Most Popular Genres in Intervals')
plt.show()
```


    
![png](Visualizations/Visualizations/Visualizations/output_83_0.png)
    



```python
count_genres_interval.genres[count_genres_interval.popularity.idxmax()]
```




    'Action|Adventure|Science Fiction|Thriller'



- From 1960 to 1995, the most popular genres is  Action|Adventure|Science Fiction|Thriller
- From 1995 to 2004, the most popular genres is  Adventure|Action|Science Fiction
- From 2004 to 2010, the most popular genres is  Action|Thriller|Science Fiction|Mystery|Adventure
- From 2010 to 2015, the most popular genres is  Fantasy|Action|Thriller

Action|Adventure|Science Fiction|Thriller is the most popular genres in all intervals.

### 10.What kinds of properties are associated with movies that have high revenues?


```python
df.head(1)
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
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>director</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
      <th>years_intervals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.985763</td>
      <td>150000000.0</td>
      <td>1.513529e+09</td>
      <td>Jurassic World</td>
      <td>Colin Trevorrow</td>
      <td>124.0</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>2015-06-09</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
      <td>2010:2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
revenue_mean = df.revenue.mean()
high_revenue = df.query('revenue > @revenue_mean')
```


```python
high_revenue.head()
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
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>director</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
      <th>years_intervals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.985763</td>
      <td>150000000.0</td>
      <td>1.513529e+09</td>
      <td>Jurassic World</td>
      <td>Colin Trevorrow</td>
      <td>124.0</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>2015-06-09</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
      <td>2010:2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>28.419936</td>
      <td>150000000.0</td>
      <td>3.784364e+08</td>
      <td>Mad Max: Fury Road</td>
      <td>George Miller</td>
      <td>120.0</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Village Roadshow Pictures|Kennedy Miller Produ...</td>
      <td>2015-05-13</td>
      <td>6185</td>
      <td>7.1</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>3.481613e+08</td>
      <td>2010:2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.112507</td>
      <td>110000000.0</td>
      <td>2.952382e+08</td>
      <td>Insurgent</td>
      <td>Robert Schwentke</td>
      <td>119.0</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>Summit Entertainment|Mandeville Films|Red Wago...</td>
      <td>2015-03-18</td>
      <td>2480</td>
      <td>6.3</td>
      <td>2015</td>
      <td>1.012000e+08</td>
      <td>2.716190e+08</td>
      <td>2010:2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.173104</td>
      <td>200000000.0</td>
      <td>2.068178e+09</td>
      <td>Star Wars: The Force Awakens</td>
      <td>J.J. Abrams</td>
      <td>136.0</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>Lucasfilm|Truenorth Productions|Bad Robot</td>
      <td>2015-12-15</td>
      <td>5292</td>
      <td>7.5</td>
      <td>2015</td>
      <td>1.839999e+08</td>
      <td>1.902723e+09</td>
      <td>2010:2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.335014</td>
      <td>190000000.0</td>
      <td>1.506249e+09</td>
      <td>Furious 7</td>
      <td>James Wan</td>
      <td>137.0</td>
      <td>Action|Crime|Thriller</td>
      <td>Universal Pictures|Original Film|Media Rights ...</td>
      <td>2015-04-01</td>
      <td>2947</td>
      <td>7.3</td>
      <td>2015</td>
      <td>1.747999e+08</td>
      <td>1.385749e+09</td>
      <td>2010:2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
high_revenue.director.value_counts()
```




    Steven Spielberg                 23
    Robert Zemeckis                  12
    Ridley Scott                     10
    Michael Bay                      10
    Clint Eastwood                   10
                                     ..
    Gareth Edwards                    1
    Richard Marquand                  1
    Jon Amiel                         1
    Peter Farrelly|Bobby Farrelly     1
    NimrÃ³d Antal                     1
    Name: director, Length: 522, dtype: int64



Most of these movies are made by Steven Spielberg


```python
high_revenue.production_companies.value_counts()[:10]
```




    Paramount Pictures                                    22
    DreamWorks Animation                                  13
    Walt Disney Pictures|Pixar Animation Studios          13
    Universal Pictures                                    13
    Eon Productions                                       10
    Walt Disney Pictures                                   9
    Walt Disney Pictures|Walt Disney Feature Animation     9
    Columbia Pictures                                      8
    Imagine Entertainment|Universal Pictures               8
    Marvel Studios                                         8
    Name: production_companies, dtype: int64



Most of these movies are produced by Paramount Pictures.


```python
high_revenue.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 1092 entries, 0 to 10760
    Data columns (total 15 columns):
     #   Column                Non-Null Count  Dtype         
    ---  ------                --------------  -----         
     0   popularity            1092 non-null   float64       
     1   budget                1092 non-null   float64       
     2   revenue               1092 non-null   float64       
     3   original_title        1092 non-null   object        
     4   director              1092 non-null   object        
     5   runtime               1092 non-null   float64       
     6   genres                1092 non-null   object        
     7   production_companies  1092 non-null   object        
     8   release_date          1092 non-null   datetime64[ns]
     9   vote_count            1092 non-null   int64         
     10  vote_average          1092 non-null   float64       
     11  release_year          1092 non-null   int64         
     12  budget_adj            1092 non-null   float64       
     13  revenue_adj           1092 non-null   float64       
     14  years_intervals       1092 non-null   category      
    dtypes: category(1), datetime64[ns](1), float64(7), int64(2), object(4)
    memory usage: 129.2+ KB
    


```python
high_revenue.release_year.value_counts()[:25]
```




    2011    67
    2013    59
    2014    59
    2012    56
    2010    55
    2008    51
    2015    48
    2006    46
    2004    46
    2003    46
    2007    45
    2009    45
    2005    42
    2002    40
    2000    36
    1997    35
    2001    32
    1998    30
    1999    29
    1995    28
    1996    25
    1993    21
    1994    20
    1992    16
    1989    13
    Name: release_year, dtype: int64



Most of the movies with high revenue are released in the interval from 1995 to 2011.


```python
high_revenue.describe()
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
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>runtime</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1092.000000</td>
      <td>1.092000e+03</td>
      <td>1.092000e+03</td>
      <td>1092.000000</td>
      <td>1092.000000</td>
      <td>1092.000000</td>
      <td>1092.000000</td>
      <td>1.092000e+03</td>
      <td>1.092000e+03</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.202657</td>
      <td>7.465807e+07</td>
      <td>2.959808e+08</td>
      <td>115.624542</td>
      <td>1251.977106</td>
      <td>6.390842</td>
      <td>2003.288462</td>
      <td>8.366946e+07</td>
      <td>3.595926e+08</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.224026</td>
      <td>5.464514e+07</td>
      <td>2.413990e+08</td>
      <td>21.172117</td>
      <td>1285.774769</td>
      <td>0.708161</td>
      <td>9.443068</td>
      <td>5.437873e+07</td>
      <td>2.940109e+08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.131526</td>
      <td>1.130000e+02</td>
      <td>1.094236e+08</td>
      <td>72.000000</td>
      <td>14.000000</td>
      <td>4.200000</td>
      <td>1961.000000</td>
      <td>2.248029e+02</td>
      <td>1.029637e+08</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.074580</td>
      <td>3.500000e+07</td>
      <td>1.509260e+08</td>
      <td>99.750000</td>
      <td>393.250000</td>
      <td>5.900000</td>
      <td>1998.000000</td>
      <td>4.162841e+07</td>
      <td>1.761617e+08</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.617808</td>
      <td>6.000000e+07</td>
      <td>2.119945e+08</td>
      <td>113.000000</td>
      <td>792.500000</td>
      <td>6.400000</td>
      <td>2005.000000</td>
      <td>7.273568e+07</td>
      <td>2.595131e+08</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.564112</td>
      <td>1.000000e+08</td>
      <td>3.489863e+08</td>
      <td>128.000000</td>
      <td>1658.750000</td>
      <td>6.900000</td>
      <td>2011.000000</td>
      <td>1.146804e+08</td>
      <td>4.323176e+08</td>
    </tr>
    <tr>
      <th>max</th>
      <td>32.985763</td>
      <td>3.800000e+08</td>
      <td>2.781506e+09</td>
      <td>201.000000</td>
      <td>9767.000000</td>
      <td>8.300000</td>
      <td>2015.000000</td>
      <td>3.683713e+08</td>
      <td>2.827124e+09</td>
    </tr>
  </tbody>
</table>
</div>



**The properties of movies that have high revenue**
- Most of these movies are produced by Paramount Pictures.
- Most of the movies are released in the interval from 1995 to 2011.
- Most of these movies are directed by Steven Spielberg.
- The movies have a high budget.
- Runtime doesn't exceed 201 and not less than 72.
- The vote count doesn't exceed 9767 and this is the maximum number of the vote counts.

<a id='conclusions'></a>
## Conclusions

After digging deep into these data, do some statistical analysis, and answer some question, here they are the insights I got:  
- Most of the movies in this dataset are comedy and drama movies.
- In 2011 over 175 movies have been released, and this the most number of movies released in a specific year.
- The number of movies increases over years.
- Paramount Pictures company has released the most number of movies.
- These movies take 109.35 minute on average.
- The popularity and revenue are increases with the budget of the movie. The more budget is, the more popularity and revenue are
- The average rating of movies is getting worse over the years, which means the old movies get high ratings than the new ones.
- From 1960 to 1995, the most popular genres is Action|Adventure|Science Fiction|Thriller
- From 1995 to 2004, the most popular genres is Adventure|Action|Science Fiction
- From 2004 to 2010, the most popular genres is Action|Thriller|Science Fiction|Mystery|Adventure
- From 2010 to 2015, the most popular genres is Fantasy|Action|Thriller
- Action|Adventure|Science Fiction|Thriller is the most popular genres in all intervals.
- The increase in vote count causes an increase in popularity.
- **The properties of movies that have high revenue**

   - Most of these movies are produced by Paramount Pictures.
   - Most of the movies are released in the interval from 1995 to 2011.
   - Most of these movies are directed by Steven Spielberg.
   - The movies have a high budget.
   - Runtime doesn't exceed 201 and not less than 72.
   - The vote count doesn't exceed 9767 and this is the maximum number of the vote counts.
   
 **Limitations**
- All insights are limited to the underlying data set, and they can't be generalized. Taking into account, a large number of entries have been removed due to missing values.

#### Some Important Graphs

- **Most of the movies in this dataset are comedy and drama movies.**
![number_movies.png](Visualizations/Visualizations/number_movies.png)

- **These movies take 109.35 minute on average.**
![runtime.png](Visualizations/Visualizations/runtime.png)

- **The popularity and revenue are increases with the budget of the movie. The more budget is, the more popularity and revenue are**
![popularity_budget.png](Visualizations/Visualizations/popularity_budget.png)

![revenue_budget.png](Visualizations/Visualizations/revenue_budget.png)

- **The average rating of movies is getting worse over the years, which means the old movies get high ratings than the new ones.**
![AverageRating_Years.png](Visualizations/Visualizations/AverageRating_Years.png)
