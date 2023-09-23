from scheduler import schedul_date_check
from datetime import datetime, timedelta
import calendar
today=datetime.today().date()
check_date=schedul_date_check
check_date.check_new_date(today)
