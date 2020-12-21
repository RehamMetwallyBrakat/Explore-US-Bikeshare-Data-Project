import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday','wednesday','thursday','friday','saturday','sunday','all']

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
    city = input('Enter the city (chicago, new york city, washington) : ').lower()
    while city not in CITY_DATA:
        city = input('Enter the city (chicago, new york city, washington) : ').lower()
                

    # get user input for month (all, january, february, ... , june)
    month =input('Enter the month (all, january, february, ... , june): ').lower()
    while month not in MONTHS:
        month =input('Enter the month (all, january, february, ... , june): ').lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of the week (all, monday, tuesday, ... sunday): ').lower()
    while day not in DAYS:
        day = input('Enter the day of the week (all, monday, tuesday, ... sunday): ').lower()


   
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
    # read city csv file
    df = pd.read_csv(CITY_DATA[city])
    # convert start time text to datetime formate
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month , day of week and hour from start time column to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['Start To End'] = df['Start Station']+" to "+df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is : ', df['month'].mode()[0])

    # display the most common day of week
    print('The most common day is : ', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('The most common hour is : ', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station is ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is ', 
          df['Start To End'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is ', df['Trip Duration'].sum())

    # display mean travel time
    print('Mean travel time is ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city,df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types ',df['User Type'].value_counts())
    
    if city != 'washington':
        # Display counts of gender
        print('Gender ',df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is {} ,the most recent year of birth is {} and most common year of birth is {}'
              .format(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    '''
    Displaying random five raws from our dataframe
    Args:
        (df) DataFrame
   
    '''
    while True:
        display=input("Would you like to display raw data?Yes/No ").lower()
        if display == 'yes':
            s = df.sample(n = 5) 
            print(s)
        elif display == 'no':break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city,df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
