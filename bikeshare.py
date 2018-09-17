import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    city = ' '
    while(city.lower() not in CITY_DATA):
        city = input('\nEnter name of the city to analyze: ').lower()
        if city not in CITY_DATA:
            print('\nInvalid Input! You have not entered a correct city name. Try again..')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    month = ' '
    if month !=  'all':
        while(month.lower() not in months):
            month = input('\nEnter name of month to analyze: ').lower()
            if month not in months:
                print('\nInvalid month! You have not entered a correct month name. Try again..')
            else:
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ' '
    if day !=  'all'
        while(day.lower() not in days):
            day = input('\nEnter the day of week: ').lower()
            if day not in days:
                print('\nInvalid day of week! You have not entered a correct day of the week. Try again..')
            else:
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
    df['hour'] = df['Start Time'].dt.hour
    df['week_day'] = df['Start Time'].dt.weekday

    # filter by month to create the new dataframe
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month']] == month

    # filter by day of week to create the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month:', df['month'].mode()[0])

    # display the most common day of week
    print('The most common day of week:', df['week_day'].mode()[0])

    # display the most common start hour
    print('The most common start hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    num_trips = df.groupby(['Start Station', 'End Station']).size()
    print('The most frequent combination of start station and end station trip:\n', num_trips[num_trips == num_trips.max()])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # display mean travel time
    print("\nMean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('\nThe \'Gender\' and \'Birth Year\' information is not available for Washington.')
    else:
        # Display counts of gender
        print('\nCounts of gender:\n', df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: ', int(df['Birth Year'].min()))
        print('\nMost common year of birth: ', int(df['Birth Year'].mode()[0]))
        print('\nMost recent year of birth: ', int(df['Birth Year'].max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            show_data = input('\nDo you want to explore the raw data? Enter yes or no.\n')
            if show_data.lower() != 'yes':
                break
            else:
                print('\nAfter applying filters, the dataset for {} contains {} rows.'.format(city,df.shape[0]))
                n = int(input('\nEnter the number of rows of data you would like to display: '))
                print('The raw data is displayed below as requested.\n', df.head(n))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
