import datetime

date = datetime.datetime.now() # current date with time & seconds
print(date)

date = datetime.date(2025,8,31) # custom date
print(date)

today = datetime.date.today() # gives today's date
print(today)

datef = datetime.datetime.now().strftime("%H:%M:%S") # formating the time 
print(datef)

# Parsing Strings to Date (strptime)
dt = datetime.datetime.strptime("2025-08-31 22:36", "%Y-%m-%d %H:%M")
print(dt)

# Date Arithmetic (timedelta), For adding or subtracting days/hours.

tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
due_date = today + datetime.timedelta(days=30)
print(due_date)

# Extracting Parts of Date/Time
now = datetime.datetime.now()
print(now.year)   # 2025
print(now.month)  # 9
print(now.day)    # 1
print(now.hour)   # 14
print(now.weekday())  # 0 = Monday

# -----------------------
# Working with Time Zones (pytz)

import pytz

utc_now = datetime.datetime.now(pytz.utc) # utc date & time
print(utc_now)

