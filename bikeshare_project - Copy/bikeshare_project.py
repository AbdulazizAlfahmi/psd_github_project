import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if (city in ['chicago', 'new york city', 'washington']):
            break
        print('Ops invalid entry , please try again')

    while True:

        filter1 = input(
            'Would you like to filter the data by month, day, both  or not at all?\n').lower()
        if (filter1 in ['day', 'both', 'month', 'not at all']):
            break
        print('Ops invalid entry , please try again')

    if filter1 == 'month':

        while True:
            month = input(
                'Please input the name of the month you want to filter by(e.g January,April...)\n').lower()
            day = 'not at all'
            if (month in ['january', 'february', 'march', 'april', 'may', 'june', 'not at all']):
                break
            print('Ops invalid entry , please try again')

    elif filter1 == 'day':
        while True:
            day = input(
                'Please input the name of the day you want to filter by(e.g Saturday,monday..)\n').title()
            month = 'not at all'

            if (day in ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'not at all']):
                break
            print('Ops invalid entry , please try again')

    elif filter1 == 'both':
        while True:
            month = input(
                'Please input the name of the month you want to filter by(e.g January,April...)\n').lower()
            if(month in ['january', 'february', 'march', 'april', 'may', 'june', 'not at all']):
                break
            print('Ops invalid entry , please try again')

        while True:
            day = input(
                'Please input the name of the day you want to filter by(e.g Saturday,monday..)\n').title()
            month = 'not at all'
            if(day in ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'not at all']):
                break
            print('Ops invalid entry , please try again')

    elif filter1 == 'not at all':
        day = 'not at all'
        month = 'not at all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'not at all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'not at all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    nm = df['month'].mode()[0]
    m_month = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    m_day = df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    m_hour = df['hour'].mode()[0]

    print('Most common month is {}\nand most common day is {}\nand most common hour is {}'.format(
        m_month[nm], m_day, m_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    ms_station = df['Start Station'].mode()[0]

    es_station = df['End Station'].mode()[0]

    cs_station = (df['Start Station'] + df['End Station']).mode()[0]

    print('The most common\nStart Station: {}\nEnd station: {}\ncombination stations: {}'.format(
        ms_station, es_station, cs_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = int(df['Trip Duration'].sum(axis=0, skipna=True))

    average_travel_time = int(df['Trip Duration'].mean(axis=0, skipna=True))

    print('Total duration time is: {} hours\nMean of travel time is: {} Min(s)'.format(
        total_travel_time//60, average_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()

    if 'Birth Year' in df:
        user_gender = df['Gender'].value_counts()

        Ebirth = int(df['Birth Year'].min())

        Mbirth = int(df['Birth Year'].max())

        Cbirth = int(df['Birth Year'].mode()[0])
        print('The count of genders is  as follows \n{}\nThe earliest birth was in {}'.format(
            user_gender, Ebirth))
        print('The yengest user was born in {}\nThe most year the users were born in is :{} '.format(Mbirth, Cbirth))

    print('The count of users is as follows\n{}'.format(user_types))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def rawdata(df):
    x = input('If you want to see 5 rows of the raw data write "yes" , otherwise write "no"\n')
    y = 0
    z = 5
    while x == 'yes':
        print(df.iloc[y:z])
        y += 5
        z += 5
        x = input('if you eant to see more 5 rows of the raw data enter "yes" , otherwise write  "no" \n')


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
