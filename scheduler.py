
from datetime import datetime, timedelta
import calendar

class schedul_date_check:
    global n
    n=1
    global check_holiday
    check_holiday=('Saturday','Sunday')
    def get_next_date(Next_date):
        Next_Date = Next_date + timedelta(days=n+1)
        return Next_Date

    def check_new_date(Next_Date):
        if (calendar.day_name[Next_Date.weekday()] in check_holiday):
            print(Next_Date,'is holiday',calendar.day_name[Next_Date.weekday()])
            check_date=schedul_date_check.get_next_date(Next_Date)
            schedul_date_check.check_new_date(check_date)
            return Next_Date,'Holiday'
        else:

            print(Next_Date,'Is working Day you Can visit')
            return Next_Date,'Working'
