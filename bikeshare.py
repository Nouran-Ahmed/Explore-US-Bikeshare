import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['January', 'February', 'March', 'April', 'May', 'June', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Come explore US Bike data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Choose a city from chicago, new york city, or washington: ").lower()
        if city in cities:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month or all, eg. January: ")
        if month in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']
    while True:
        day = input("Choose a day or all, eg: Sunday: ")
        if day in week:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = months.index(month) + 1
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day]
    return df
                    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    #print("The common month is: " , df['month'].mode()[0])
    print("Common month is: " , months[common_month])

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    #print("The most common day is: " , df['day_of_week'].mode()[0])
    print("Common day of week is: " , common_day_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    #print("The most common start hour is: " , df['hour'].mode()[0])
    print("Common hour is: " , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #common_start_station = df['Start Station'] .mode()[0]
    print("The most common start station is: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    #common_end_station = df['End Station'] .mode()[0]
    print("The most common end statuon is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end_station = df['Start Station'], df['End Station'].mode()[0]
    print("The most frequent combination of start and end stations is: ", df[['Start Station', 'End Station']].mode().loc[0][0], "and", df[['Start Station', 'End Station']].mode().loc[0][1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #total_travel_time = df['Trip Duration'] .sum()
    print("The total travel time is: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    #mean_travel_time = df['Trip Duration'] .mean()
    print("The mean travel time is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #user_type_count = df['User Type'] .value_counts()
    print("The user type count is: ", df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if city is 'chicago' or city is 'new york city':
        #gender_count = df['Gender'] .value_counts()
        print("The gender count is: ", df['Gender'].value_counts())
        print("The earliest birth year is: ", df['Birth Year'].min())
        print("The most recent birth year is: ", df['Birth Year'].max())
        print("The most common birth year is: ", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()
