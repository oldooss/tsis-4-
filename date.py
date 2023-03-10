#1
from datetime import date, timedelta, time, datetime

fiveDaysFromCurrentDate = date.today() - timedelta(5)

print(f"Todays date : {date.today()}")
print(f"5 days before Current Date : {fiveDaysFromCurrentDate}")

#2

print(date.today() - timedelta(1))
print(date.today())
print(date.today() + timedelta(1))

#3

dropMicroSec = datetime.today().replace(microsecond=0)
print(dropMicroSec)

#4

def dateInDeffSec(date2, date1):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2023-03-8 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()

print(dateInDeffSec(date2, date1), "seconds")
