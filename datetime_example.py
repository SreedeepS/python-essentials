
import time
import calendar #provides additional information about calendar years; that is, how many days there are in a month
import datetime as dt #differentiate the datetime module from the datetime class
from dateutil import tz #Dateutil is not a module from the standard library

#To create a datetime with a time zone, you just need to pass it through the tzinfo argument:
#Create a datetime for April 24, 1989, at 11 a.m. in Madrid.
d1 = dt.datetime(1989, 4, 24, hour=11, tzinfo=tz.gettz("Europe/Madrid")) 

d2 = dt.datetime(1989, 4, 24, hour=8, tzinfo=tz.gettz("America/Los_Angeles")) 

print('d1.hour > d2.hour:',d1.hour > d2.hour) 
#The time zone for d1 and d2 is different, and 8 in Los Angeles happens after 11 in Madrid.
print('d1 > d2:',d1 > d2) #Even though hour is greater, date wise d1 is less than d2. 

#Convert a datetime from one time zone to another
d2_madrid = d2.astimezone(tz.gettz("Europe/Madrid"))
print('Los Angeles time - ',d1, ', converted to Madrid timezone: ',d2_madrid)

'''
Use UTC to work with timestamps, with time not related to any location.
UTC is Coordinated Universal Time and is a system that provides a universal way of coordinating
time across locations. Most common standard for the time. If you use any specific time zone, you 
should be aware that nations might change the time at any point, which could make any of your calculations invalid.
'''
#Find out the difference in seconds between two important events

d1 = dt.datetime(2019, 2, 25, 10, 50, tzinfo=dt.timezone.utc)
d2 = dt.datetime(2019, 2, 26, 11, 20, tzinfo=dt.timezone.utc)
print('Difference b/w d2 and d1:',d2-d1)
#translated to the total number of seconds by calling total_seconds in the time delta object that the subtraction returns

td = d2 - d1
print('Difference in seconds:',td.total_seconds())

'''
To send datetime objects in formats such as JSON or others that do not support native datetimes,
a common way to serialize datetime is by encoding them in a string using the ISO 8601 standard. 
This can be done by using isoformat, which will output a string, and parsing them with the fromisoformat method.
'''

d1 = dt.datetime.now(dt.timezone.utc)
print("Datetime in ISO format:",d1.isoformat())

#Get current time. Example using both datetime and time
time_now = time.time() 

#Use the UTC time zone when getting time with datetime. 
#This is necessary because time.time returns Unix time, which uses an epoch that is in UTC.
datetime_now = dt.datetime.now(dt.timezone.utc)

#Calculate the epoch by subtracting datetime and a time delta
epoch = datetime_now - dt.timedelta(seconds=time_now)
print(epoch) #The result is the Unix epoch — January 1, 1970, the date from when Unix time is counted.

#Create a calendar and get all of the days in a month
c = calendar.Calendar()
print(list(c.itermonthdates(2019, 2)))
print('---'*30)
#Above function returns all date instances for all the weeks in the month, if you want to get only 
# the days that belong to the specific month, you need to filter them.
print(list(d for d in c.itermonthdates(2019, 2) if d.month == 2))
print('---'*30)