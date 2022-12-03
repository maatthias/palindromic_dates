
# first iteration
import datetime

start_date = datetime.datetime.now()
days_to_check = 30
date_to_check = start_date

for x in range(days_to_check):
    if int(date_to_check.strftime("%d")[::-1]) < 24 and int(date_to_check.strftime("%m")[::-1]) < 60:
        print(date_to_check.strftime("%Y-%m-%d") + " " + (date_to_check.strftime("%Y.%m:%d")[::-1]))
    date_to_check = date_to_check + datetime.timedelta(days=1)


# second iteration
import datetime
from dateutil.parser import parse as parse_date

start_date = datetime.datetime.now()
days_to_check = 30
date_to_check = start_date
count_of_valid_dates = 0

for x in range(days_to_check):
    string_to_parse = date_to_check.strftime("%Y-%m-%d") + " " + (date_to_check.strftime("%Y.%m:%d")[::-1])
    try:
        parse_date(string_to_parse)
        count_of_valid_dates += 1
    except ValueError:
        print("\tnot a valid date")
    date_to_check = date_to_check + datetime.timedelta(days=1)

print(f"count_of_valid_dates is {count_of_valid_dates}")
