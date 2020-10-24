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

    city = input("For which city do you want to see data: ")
    while city.lower() not in ('chicago', 'new york city', 'washington'):
        city = input('Thats not a valid city! Please enter chicago, new york city, washington: ')
        if not city:
            print("Sorry, I didn't catch that. Enter again: ")
    city = city.lower()

    print("Thank you! You choosed " + city +" !")


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("For which month do you want to see data: ")
    while month.lower() not in ('january', 'febuary', 'march', 'april', 'may', 'june', 'all' ):
        month = input('Thats not a valid month! Please enter january, febuary, march, ... , june or "all": ')
        if not month:
            print("Sorry, I didn't catch that. Enter again: ")
    month = month.lower()
    print("Thank you! You choosed " + month +" !")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("For which day of the week do you want to see data: ")
    while day.lower() not in ('monday', 'tuesday', 'wendsday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        day = input('Thats not a valid day! Please enter monday, tuesday, wendsday, ... or all: ')
        if not day:
            print("Sorry, I didn't catch that. Enter again: ")
    day = day.lower()
    print("Thank you! You choosed " + day +" !")

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
    if city in CITY_DATA:
        df = pd.read_csv(CITY_DATA[city])
    else:
        print("Error while loading the Files, please restart the Programm")

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    # extract hour from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.day

    # find the most popular day
    popular_day = df['day'].mode()[0]

    print('Most Popular Start day:', popular_day)


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_startstation = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['combistations'] = df['Start Station'] + df['End Station']
    popular_combistation = df['combistations'].mode()[0]

    print('Most Popular combinaton of start and End Stations:', popular_combistation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel Time'].mode()[0]

    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print('Mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(city)
    if city == 'washington':
        print('There are no user stats available for washington')
    else:
        # TO DO: Display counts of user types
        df['Counter'] = 1
        print('\nThe number of users divided by usertype:')
        print(df.groupby(['User Type'])['Counter'].sum())
        print('-'*10)

        # TO DO: Display counts of gender
        print('\nThe number of users divided by gender:')
        print(df.groupby(['Gender'])['Counter'].sum())
        print('-'*10)

        # TO DO: Display earliest, most recent, and most common year of birth
        popular_birth_year = df['Birth Year'].mode()[0]
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()

        print('\nOther user stats:')
        print('Most Popular Birth Year:', popular_birth_year)
        print('Minimum Birth Year:', oldest)
        print('Most recent Birth Year:', youngest)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data_quest(df):
    row_selection_start = 0
    row_selection_end = 5
    rawdata_input = input('\nWould you like to see raw data? Enter yes or no.\n')
    #check input yes or no
    while rawdata_input.lower() not in ('yes', 'no'):
        rawdata_input = input('Thats not a valid input! Please enter yes or no.\n')
    while rawdata_input != 'no':
        print(df.iloc[row_selection_start:row_selection_end])
        row_selection_start += 5
        row_selection_end += 5
        rawdata_input = input('\nWould you like to see more raw data? Enter yes or no.\n')
    print('Okay, thank you!')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data_quest(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
