import datetime as dt

date = dt.datetime.now()

month = date.month
year = date.year
day = date.day
hour = date.hour
min = date.minute
day_of_week = date.weekday()


if date.year == 2025:
    print(date.year)
    print(month)
    print(day)
    print(hour)
    print(min)
    print(date.second)
    print(day_of_week)
    print(date)

print(type(date))
print(type(year))


date_of_birth = dt.datetime(year = 2025, month = 1, day = 13, hour = 18)
print(date_of_birth)