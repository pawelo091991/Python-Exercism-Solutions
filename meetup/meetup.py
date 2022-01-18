from datetime import date
from datetime import timedelta


DAY = {
    "Monday"    : 0,
    "Tuesday"   : 1,
    "Wednesday" : 2,
    "Thursday"  : 3,
    "Friday"    : 4,
    "Saturday"  : 5,
    "Sunday"    : 6
}

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):

    # Convert name of day to number
    day_of_week = DAY[day_of_week]
       
    if week == "teenth":
        # Start searching from 13th
        currDate = date(year, month, 13)
        # go to next day if conditions to find correct day in while loop are not fullfiled
        while day_of_week != currDate.weekday() and currDate.day >= 13 and currDate.day < 20:
            currDate += timedelta(days=1)

    elif week == "last":
        # Start from next month 
        currDate = date(year, month, 1)
        currDate += timedelta(days=31)
        # go to previous day if conditions to find correct day in while loop are not fullfiled
        while currDate.weekday() != day_of_week or currDate.month != month:
            currDate += timedelta(days=-1)

    else:
        # Start searching from first day in month
        currDate = date(year, month, 1)
        # Find first occurance of weekday
        while currDate.weekday() != day_of_week:
            currDate += timedelta(days=1)
        # Add weeks to find the date
        currDate += timedelta(days=7*(int(week[0])-1))
        

    
    # If we somehow end up in incorrect year, month or day, raise exception
    if currDate.year != year or currDate.month != month:
        raise MeetupDayException("That day does not exist.")

    # Return the date
    return currDate
