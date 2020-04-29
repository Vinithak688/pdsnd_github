import time
import pandas as pd
import numpy as np
import calendar

pd.set_option('precision', 2)


print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
st_time= time.time()
while True:
    city = str(input("Would you like to see data for Chicago, New York or Washington?"))
    city = city.lower()
    city= city.replace(" ", "")
    if city == 'newyork':
        city= new_york_city

    b = city in ['chicago', 'new_york_city', 'washington']
    if not b:
        print("Enter a valid city name")
        continue
    else:
        break
# loading the data into variable data from the below code
data= pd.read_csv('{}.csv'.format(city))


#Creating four new column names in the data dataframe extracting date, year, monthname, weekday(number)

data['Date']= pd.to_datetime(data['Start Time'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Month'] = data['Month'].apply(lambda x: calendar.month_name[x])
data['Day'] = data['Date'].dt.day
data['Hour'] = data['Date'].dt.hour
s=data['Date']

#And according to our project- Sunday should be 1 so I manipulated to match the given scenario.
data ['Weekday'] = data['Date'].dt.dayofweek + 2
print("\nTime to load the data is:", time.time()- st_time )
print("\nData from the selected city is loaded and ready to be analysed!")

# function to load the data using user input as filters
def load_data():

    """
    Input: There is no any input to the function.
    Output: The function returns the data after applying the month, day filters from the user.

    """

    filter= input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter.')

    # get user input for month (all, january, february, ... , june)
    if filter=='month':
        month = str(input("Which month? January, February, March, April, or June?"))
        month= month.title()
        #filtering the data by month
        df= data[(data['Month']==month)]

    if filter=='day':
        wday = int(input("Which day? Please type your response ad an integer between 1 to 7(e.g. , 1= Sunday)."))
        #filtering the data by day
        df= data[data['Weekday']==wday]
    if filter=='both':
        month = str(input("Which month? January, February, March, April, or June?"))
        wday = int(input("Which day? Please type your response ad an integer (e.g. , 1= Sunday)."))
        df= data[ (data['Month']== month) & (data['Weekday']== wday) ]
    if filter=='none':
        df= data

    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nCommon month is",df['Month'].mode()[0])

    # display the most common day of week
    print("\nCommon day of week is",df['Day'].mode()[0])

    # display the most common start hour
    print("\nCommon start hour is",df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    mcs= df['Start Station'].mode()[0]

    print("The most common start station is: ",mcs)

    # display most commonly used end station
    mce= df['End Station'].mode()[0]
    print("The most common end station is: ",mce)

    # display most frequent combination of start station and end station trip
    s = list(df['Start Station'])

    e = list(df['End Station'])

    t= tuple(zip(s,e))

    myDict = {}

    for item in t:
        myDict[item] = myDict.get(item, 0) + 1

    m=max(myDict, key=myDict.get)

    print("The combination is: \n",m, "Count is: " , myDict[m])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\nThe total travel time is: ", df['Trip Duration'].sum())

    # display mean travel time
    print("\nThe mean travel time is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print("\nCount of User types is:",df['User Type'].value_counts())

    # Display counts of gender
    print("\nCount of Users by Gender is:",df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    MinYear = int(df['Birth Year'].min())

    print("\nThe earliest year of birth is: ",MinYear)

    MaxYear = int(df['Birth Year'].max())

    print('\nRecent birth year is: ',  MaxYear  )

    print("\nMost common birth year is: ", int(df['Birth Year'].mode()) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        df = load_data()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        seedata = input('\nWould you like to look at the data? Enter yes or no.\n')
        a=0
        b = a+5
        moredata = 'no'
        if seedata == 'yes':
            while True:
                print(df.iloc[a:b])
                a = a+5
                b= a+5
                moredata = input("Would you like to look 5 more rows of the data? Enter yes or no.\n")
                if moredata.lower() != 'yes':
                    break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
