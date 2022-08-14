import time
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #lists of months and days
   
    days = ['tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ,'sunday','monday','all']
    months = ['january', 'february', 'march', 'april', 'may' ,'june','all']
    
    
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("please Enter name of City [Chicago , New York City, Washington]\n").lower()
        if city not in CITY_DATA:
            print("Please Enter the correct City Name!!")
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True :
        month = input("Please Enter which month [ 'January', 'February', 'March', 'April', 'May' ,'June'] to filter by, or 'all' to apply no month filter\n").lower()
        if month not in months and month != 'all':
            print("Please Enter corrert Month Name !!")
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("Please Enter which day of week to filter by['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ,'Sunday'], or 'all' to apply no day filter\n").lower()
        if day not in days and day != 'all':
            print("Please Enter correct Day Name")
        else:
            break
    print('-'*40)
    print("loading... ... ")
    return(city, month, day) 


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
    #read cvs file
    df =pd.read_csv(CITY_DATA[city])
    
    #convert Start Time column to date Time
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    #extract month from date 
    #dt. month attribute return a numpy array containing the month of the datetime in the underlying data of the given series object
    df['month']=df['Start Time'].dt.month
    
    #extract day from date 
    #day_name()    Returns the name of the day of the week.
    df['day_name']= df['Start Time'].dt.day_name()
    
    #fliter by month if it applicable
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may' ,'june']
        
        #dt.month retuns intgers so we need to get name of month by number of index
        month=months.index(month)+1
        #Filter by month and create new DataFarm have month
        df =df[df['month'] == month]

    #fliter by day if it applicable
    if day != 'all':
        #Filter by day and create new DataFarm have Weekday
        df = df[df['day_name'] == day.title()]

    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
         popular_month_int =df['month'].mode()[0]
         months=['january', 'february', 'march', 'april', 'may' ,'june']
         popular_month_name= months[popular_month_int -1]
         print("The most commn month is {}".format( popular_month_name))
    else:
        print("The most popular month is showen when you selecr 'ALL'")

    # display the most common day of week
    if day =='all':
        popular_day =df['day_name'].mode()[0]
        print("The most commn day is {}".format(popular_day ))
    else:
        print("The most popular day is showen when you selecr 'ALL'")

    # display the most common start hour
    
    df['hour']= df['Start Time'].dt.hour
    popular_hour= df['hour'].mode()[0]
    print("The most commn hour is {}:00".format(popular_hour))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print("The common used Start Station "+popular_start_station)
    
    # display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print("The common used Start Station "+popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Start End station'] = df['Start Station'] + ' - ' + df['End Station']
    popular_start_end_station = df['Start End station'].mode()[0]
    print("The most frequent combination os start and end station "+ popular_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_sec = df['Trip Duration'].sum()
    total_travel_time_hour = total_travel_time_sec/3600
    print("Total Travel time is {} hours".format(total_travel_time_hour))
    
    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print("Avarage Travel time is {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print("Counts of user types {}".format(counts_user_types))

    # Display counts of gender
    if 'Gender' in df:
        counts_gender=df['Gender'].value_counts()
        print("Counts of user types {}".format(counts_gender))
    else :
        print ("No gender found")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year =df['Birth Year'].min()
        print("Earliest Year of brith is {}" .format(earliest_year))
        
        most_recent_year = df["Birth Year"].max()
        print("Most recent year of brith is {}".format(most_recent_year))
        
        most_common_year = df['Birth Year'].mean()
        print("Most common year of brith is {}".format(most_common_year))
    else :
        print ("No birth year found")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Parameters
    ----------
    df : TYPE data frame comes from load_data function
        DESCRIPTION.

    Returns rows of data
    -------
    """

    #get if user want to show 5 rows of data
    # if user enter invaild input
    choice = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0 
    while (choice) != 'yes'.lower() and (choice) != 'no'.lower():
          choice = input("invaild input!!\nPlease enter YES or No\n")
          
    #user enter corrert input
    while (choice) == 'yes'.lower():
          print(df.iloc[start_loc:start_loc+5])
          start_loc += 5
          choice =input("Would you like to continue with the next 5 rows ? Enter yes or no\n'").lower()
          while (choice) != 'yes'.lower() and (choice) != 'no'.lower():
              choice = input("invaild input!!\nPlease enter YES or No\n")
          continue 

        
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
