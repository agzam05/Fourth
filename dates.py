#1
import datetime
new_date=datetime.datetime.now()-datetime.timedelta(days=5)
print(new_date)

#2
from datetime import datetime,timedelta
yes=datetime.now()-timedelta(days=1)
today=datetime.now()
tom=datetime.now()+timedelta(days=1)
print("Yesterday:",yes)
print("Today:",today)
print("Tomorrow:",tom)

#3
from datetime import datetime
date1=datetime.now()
print(date1.strftime("%Y-%m-%d-%H-%M-%S"))

#4
from datetime import datetime, timedelta
diff=today-yes
hours=diff.total_seconds()/3600
print(hours)
