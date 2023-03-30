import datetime
import random
from calendar import monthrange

def ran_date(a, b):
    return random.randint(a, b)

'''
startDate = datetime.date(2012, 1, 1)
endDate = datetime.date.today()

print(endDate.day)

yearDate = ran_date(startDate.year, endDate.year)
monthDate = ran_date(1, 12)
print(len(str(monthDate)))
dayDate = ran_date(1, monthrange(yearDate, monthDate)[1])
print(len(str(dayDate)))
print(f"{yearDate}-{monthDate}-{dayDate}")


yearDate = ran_date(startDate.year, endDate.year)
monthDate = ran_date(1, 12)
dayDate = ran_date(1, monthrange(yearDate, monthDate)[1])

monthLen = len(str(monthDate))
if 1 == int(monthLen):
    monthDate = f"0{monthDate}"

dayLen = len(str(dayDate))
if 1 == int(dayLen):
    dayDate = f"0{dayDate}"

print(f"{yearDate}-{monthDate}-{dayDate}")

'''

cmc = "2013-02-29"
dateToday = datetime.date.today()
probDate = 0
y = int(cmc[:4])
m = int(cmc[5:7])
d = int(cmc[8:10])
maxDayDate = monthrange(y, m)[1]


if 2012 <= y <= int(dateToday.year):
    probDate = 1


if 1 <= m <= 12:
    if probDate == 1:
        probDate = 1
    else:
        probDate = 0
else:
    probDate = 0


if 1 <= d <= int(maxDayDate):
    if probDate == 1:
        probDate = 1
    else:
        probDate = 0
else:
    probDate = 0


print(probDate)


#print(today)  # 2017-05-03


