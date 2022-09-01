# problem 1 - getting the current date and time

from datetime import date, datetime

time = datetime.now()

month_arry = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = month_arry[time.month-1]

print("Today is ", month, time.day, ",", time.year)
if(time.hour <= 12):
    print("Current time is ", time.hour, ":", time.minute, ":", round(time.second, 2), "AM")
else:
    hour_arry = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    hour = hour_arry[time.hour - 13]
    print("Current time is ", hour, ":", time.minute, ":", round(time.second, 2), "PM")