import datetime

date = datetime.date(2018, 6, 25)
# 2018-06-25

today = datetime.date.today()
# 2018-07-31

fromtimestamp = datetime.date.fromtimestamp(1523027920)
# 2018-04-06

weekday = datetime.date(2018, 7, 31).weekday()
# 1 (for Tuesday)

isoweekday = datetime.date(2018, 7, 31).isoweekday()
# 2 (for Tuesday)

time = datetime.time(12, 32)
# 12:32:00

dt_today = datetime.datetime.today()
# 2018-07-31 12:52:45.989619

# dt_now = datetime.datetime.now(tz=) how to choose timezone?

ordinal = datetime.datetime.toordinal()
print(ordinal)