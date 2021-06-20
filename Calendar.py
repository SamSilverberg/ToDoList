from datetime import date
from copy import deepcopy


def weekday(date):
    '''
    Given a date as month (string), day (int), and year (int), return the weekday.
    '''
    date = date.split(' ')
    month = date[0]
    day = int(date[1])
    year = int(date[2])

    weekdays = ('Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri')
    mc = {'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 
        'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12, 'January' : 13, 'February' : 14}
    
    for k in mc.keys(): #get the value of the month
        if month == k:
            month = mc[month]
    
    if month == 13 or month == 14: #account for jan and feb
        year = year-1
    
    DoW = (day + int(((13*(month+1))/5)) + year + int((year/4)) - int((year/100)) + int((year/400))) % 7

    return weekdays[DoW]


def is_leap_year(year):
    '''
    Return True if year is a leap year; False otherwise.
    '''
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 != 0:
        return False

    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        else: 
            return False

def errors(date):
    date = date.split(' ')
    month = date[0]
    day = int(date[1])
    year = int(date[2])

    nonleap = {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30, 'May' : 31, 'June' : 30,
        'July' : 31, 'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}
    
    if nonleap.get(month) == None:
        raise ValueError
    if day < 0 or day > nonleap.get(month):
        raise ValueError
 

def day_of_year(date):
    '''
    Given a date as month (string), day (int), and year (int), return the day of the year.
    '''
    errors(date)

    date = date.split(' ')
    month = date[0]
    day = int(date[1])
    year = int(date[2])

    start_day = 0
    nonleap = {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30, 'May' : 31, 'June' : 30,
        'July' : 31, 'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}
    
    if is_leap_year(year) == True: #fix if it's a leap year
        nonleap['February'] =  29
    else:
        nonleap['February'] = 28

    for k in nonleap.keys(): #get the days not counting the current month
        if k != month:
            start_day = start_day + nonleap[k]
        elif k == month:
            break

    result = start_day + day #add the days of the current month
    return result
