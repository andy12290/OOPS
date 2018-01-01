import datetime
import pytz

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)

print(tday+tdelta)

# Birthday

bday = datetime.date(2018, 2, 12)

diff = bday - tday
print(diff)

# with new package

dt_mtn = datetime.datetime.now()
print(dt_mtn)

# conveting string into the datetime

dt_str = 'July 24, 2016'

d = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(d)


# strftime - Datetime to String
# strptime - String to Datetime
