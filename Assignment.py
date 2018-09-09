#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:03:17 2018

@author: sagar
"""

import time
from statistics import mode
import pandas as pd
import numpy as np
import datetime as dt

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
    city=get_city()
    month=get_month()
    day=get_day()
    
    
    print('-'*60)
    return city, month, day









def get_city():
    city=input ("!!WELCOME! TO EXPLORE SOME BIKESHARE OF US CITIES!!\n\n You can type Chicago , New York City Or Washinton :)\n")
    city=city.lower()
    if city == "chicago":
        return 'chicago.csv'
    if city == "new york city":
        return 'new_york_city.csv'
    if city == "washington":
        return 'washington.csv'
    else:
        print("OOPS! The entry did not match! Try again and do check your spelling!!")
        return get_city()
        

    # TO DO: get user input for month (all, january, february, ... , june)
def get_month():
    month = input("Enter the month you want with *FIRST THREE LETTER* of the month.\n")
    if month.upper()=="JAN":
        return '01'
    if month.upper()=="FEB":
        return '02'
    if month.upper()=="MAR":
        return '03'
    if month.upper()=="APR":
        return '04'
    if month.upper()=="MAY":
        return '05'
    if month.upper()=="JUN":
        return '06'
    if month.upper()=="ALL":
        return None
    else:
        print("\n Invalid Input!! Check the Spelling Human\n")
        return get_month()
         
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    day=input("\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday?\n Please Enter the day:\n")
    if day.title()== 'Sunday':
        return '0'
    if day.title()=='Monday':
        return '1'
    if day.title()== 'Tuesday':
        return '2'
    if day.title()=='Wednesday':
        return '3'
    if day.title()== 'Thursday':
        return '4'
    if day.title()=='Friday':
        return '5'
    if day.title()=='Saturday':
        return '6'
    if day.title()== 'All':
        return None
    else:
        print("\nINVALID INPUT AGAIN HUMAN!! CHECK THE SPELLING AGAIN\n")
        
    return get_day()
        
    
    
    
    
    print('-'*60)
   


def load_data(city,month,data):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Read the CSV file as asked by the user and load it into the data frame.
    df= pd.read_csv(city)
    
    #Breaking Down the time period to the dataframe to get results by filters.
    df['Start_Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start_Time'].dt.weekday_name
    df['month'] = df['Start_Time'].dt.month
    df["day_of_month"] = df["Start_Time"].dt.day
    df['Hour_Time']=df['Start_Time'].dt.hour
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')


    # TO DO: display the most common month
    month_common=mode(df['month'])
    print(" 01 : Jan \n 02 : Feb \n 03 : Mar \n 04 : Apr \n 05 : May \n 06 : Jun")
    print("Most common day is in: {}".format(month_common))
   
    # TO DO: display the most common day of week
    
    common_day=mode(df['day_of_week'])
    print("Most common day is {}.".format(common_day))
    
   
    # TO DO: display the most common start hour
    
    hours = int(df["Hour_Time"].mode())
    
    if hours == 00:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= hours < 13:
        am_pm = 'am'
        hours = pop_hour_readable
    elif 13 <= hours < 24:
        am_pm = 'pm'
        pop_hour_readable = hours - 12
    print('Most Pouplar Hour to Start is : \n{}{}.'.format(pop_hour_readable, am_pm))
     


    
   
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
   
     
    # TO DO: display most commonly used start station
    common_start_station=mode(df['Start Station'])
    print('The most popular station is {}'.format(common_start_station))
    
    # TO DO: display most commonly used end station
    common_end_station =mode(( df['End Station']))
    print('The most popular end station is {}'.format(common_end_station))
    
    
    # TO DO: display most frequent combination of start station and end station trip
    
    df['journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_pop_trip = df['journey'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))
    
    
    
    
    
    
    

   
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
 

    # TO DO: display total travel time

    travel_time=df["Trip Duration"]
    tot_travel_time= sum(travel_time)
    
    print("Total Trip Duration is {}.".format(tot_travel_time))
    
    # TO DO: display mean travel time
    
    tot_mean_time= travel_time.mean()
    print("The total mean of the travel is {}.".format(tot_mean_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    

    # TO DO: Display counts of user types
    
    user_types = df["User Type"]
    user_s= 0
    user_c= 0 
    for user in user_types:
        if user == "Subscriber":
            user_s+=1
        elif user == "Customer":
            user_c+=1
    print ("Total counts of Subscriber : {} \nTotal counts of Customer : {}".format(user_s,user_c))
   
    
    # TO DO: Display counts of gender
    
    gender_types=df["Gender"]
    gender_male=0
    gender_female=0
    for gender in gender_types:
        if gender == "Male":
            gender_male+=1
        elif gender == "Female":
            gender_female+=1
    print ("Total counts of Females : {}. \nTotal counts of Males: {}.".format(gender_female,gender_male))

    # TO DO: Display earliest, most recent, and most common year of birth
    
    
    birth_year=df["Birth Year"]
    print ("Most recent date of birth of users is : {}".format(max(birth_year)))
    print ("Most common date of birth of users is : {}".format (birth_year.mode()))
    print ("Most earlies date of birth of users is :{}".format(min(birth_year)))
    
    
    print('*'*60)
    
    
    
def main():
    while True:
        city,month,day = get_filters()
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