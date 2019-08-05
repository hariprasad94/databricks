%python

import re
from datetime import date, timedelta, datetime

start_date = "Sun Mar  7 22:45:46 2004"
end_date = "Mon Mar 8 00:11:22 2004"

date_format = "%a %b %d %H:%M:%S %Y"

logfile = "/dbfs/tmp/logs/error_log"

start_date_formatted = datetime.strptime(start_date, date_format)
end_date_formatted = datetime.strptime(end_date, date_format)

date_regex = re.compile(r'^\[(.*[0-9]{4})\].*')

with open(logfile, "r") as file:
    for line in file.readlines():
        match = date_regex.search(line)
        if match:
          matchDate = match.group(1)
          matchDate=datetime.strptime(matchDate, date_format)
          if matchDate >= start_date_formatted and matchDate <= end_date_formatted:
             print(match.string.strip())