#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']
    
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


# In[2]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']
    
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
    while city[:7] not in [city[:7] for city in CITY_DATA.keys()]:
        city = input('It seems that you entered an invalid city name. Please, enter it again.\n').lower()
        
    for cityName in CITY_DATA.keys():
        if city[:7] == cityName[:7]:
            city = cityName


   
    filter_by = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n')
    
    while filter_by.lower() not in ['month', 'day', 'both', 'none']:
        filter_by = input('Invalid value.\nWould you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n')
        
    month, day = '', ''


    # get user input for month (all, january, february, ... , june)
    if filter_by == 'month' or filter_by == 'both':
         
        month = input('Which month? January, February, March, April, May, or June? Type "all" for all months.\n').title()
        
        while month not in months and month != 'All': 
            month = input("It seems that you entered an invalid month name. Please, enter it again.\n").title()
            


    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_by == 'day' or filter_by == 'both':
        day = input('Which day?? Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday? Type "all" for all days.\n').title()
        
        while day not in days and day != 'All': 
            day = input("It seems that you entered an invalid day name. Please, enter it again.\n").title()


    print('-'*40)
    return city, month, day




def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

     # load data file into a dataframe
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[3]:



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month.lower() != 'all' and month !='':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all' and day !='':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]

    # display the most common month
    print('The most popular month: {}'.format(popular_month))
    
    # display the most common day of week
    print('The most popular day: {}'.format(popular_day))

    # display the most common start hour
    print(f'The most popular hour: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    popular_trip = df[['Start Station', 'End Station']].mode()

    print('Most Popular Station...\n')
    # display most commonly used start station
    print('Start station: {}'.format(popular_start_station))
    
    # display most commonly used end station
    print('End Station: {}'.format(popular_end_station), '\n')


    # display most frequent combination of start station and end station trip
    print('Most Popular Trip...')
    trips = df['Start Station'] + " to " + df['End Station']
    print(f'Trip: {trips.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total Duration: {total_travel_time}')


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Avg Duration: {mean_travel_time}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:





def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    for usertype, count in dict(user_type_count).items():
        print(f'{usertype}: {count}')
    print('\n')


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        for gender, count in dict(gender_count).items():
            print(f'{gender}: {count}')
        print('\n')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest_year = df['Birth Year'].min()
        youngest_year = df['Birth Year'].max()
        most_popular_year = df['Birth Year'].mode()[0]
        print('The oldest, youngest, and most popular year of birth...')
        print(f'Earliest year is {oldest_year}')
        print(f'Most recent year is {youngest_year}')
        print(f'Most popular year is {most_popular_year}')
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:

def show_individual_data(df):
    """ Print 5 rows from raw data every time"""
    choice = input("Would you like to view individual trip data?Type 'yes' or 'no'.\n").upper()
    print('\n')
    
    count = 0
    if choice.lower() == 'yes':    
        for row in df.iterrows():
            for columnName, value in dict(row[1]).items():
                print(f'{columnName}: {value}')
            print('-' * 40)
            
            count += 1
            if count % 5 == 0:
                choice = input("Would your like to view another individual trip data?Type 'yes' or 'no'.\n")
            
            if choice.lower() != 'yes':
                break
    
    
    
        


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_individual_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        print('-' * 80)
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




