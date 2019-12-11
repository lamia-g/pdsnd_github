import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Please Enter City Name (Options: 'chicago', 'new york city','washington') ")
    while city not in list(CITY_DATA.keys()):
        print("invalid input!")
        city = input("please choose one city) ")

    # TO DO: get user input for month (all, january, february, ... , june)

    MonthsList = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month = input("please choose one month or all. ")
    while month not in MonthsList:
       print("invalid input!")
       month = input("Please Enter the month or all for not specifying any month. ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DaysList = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday","all"]
    day = input("Please Enter a day or all for not specifying any day. ")
    while day not in DaysList:
       print("input is not possible!")
       day = input("Please Enter a day or all for not specifying any day. ")

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
    df['start_datetime'] = pd.to_datetime(df['Start Time'])
    df['end_datetime'] = pd.to_datetime(df['End Time'])

    df['start_end_stations_combination'] = df['Start Station'].astype(str) + " =--> " +  df['End Station'].astype(str)

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['start_datetime'].dt.month
    df['day_of_week'] = df['start_datetime'].dt.weekday_name
    df['start_time'] = df['start_datetime'].dt.time
    df['start_time_hour'] = df['start_datetime'].dt.hour

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

    # TO DO: display the most common month
    print("the most common month: " ,  df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("the most common day of week: " ,  df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print("the most common start hour: " ,  df['start_time_hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station: " ,  df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("most commonly used end station: " ,  df['Start Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station: " ,         df['start_end_stations_combination'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total traveling time: " ,  df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("travel time mean: " ,  df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types: " ,  df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("counts of gender: " ,  df['Gender'].value_counts())
    else:
        print("No data related to gender")
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("the earliest year of birth: " ,  df['Birth Year'].min(), "the most recent year of birth: ", df['Birth Year'].max(), "the most common year of birth: ", df['Birth Year'].value_counts().idxmax())
    else:
        print("No data related to birth")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    a=0
    while True:
        ask=input("would you like to see more information? (yes or no)")
        if ask.lower() == "yes":
            print(df.iloc[a:a+5])
            a+=5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
