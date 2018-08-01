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

datetime.datetime(2018, 12, 31).isoformat()
# '2018-12-31T00:00:00'

datetime.datetime(2018, 12, 31) - datetime.timedelta(days=2, hours=2)
# datetime.datetime(2018, 12, 28, 22, 0)

import pytz
dt_now = datetime.datetime.now(tz=pytz.utc)
# show time in UTC Zone