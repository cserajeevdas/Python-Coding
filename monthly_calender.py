import calendar

cal = calendar.TextCalendar(calendar.MONDAY)  
for m in range(1,13):
    print(cal.formatmonth(2020,m,0,0))
