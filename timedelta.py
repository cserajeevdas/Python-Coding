
from datetime import date
from datetime import time 
from datetime import timedelta
from datetime import datetime

def main():
    print(timedelta(days=365, hours=5, minutes=1))
    now = datetime.now()
    print("today is", now)
    print("one year from now will be: " + str(now + timedelta(days=365)))
    print("In 2 days and 1 week, it will be: " + str(now + timedelta(days=2, weeks =1)))
    t= datetime.now()-timedelta(weeks=1)
    s=t.strftime("one week ago it was "+"%A %B %d %Y")
    print(s)
    
    today = date.today()
    afd=date(today.year, 4, 1)
    if afd < today:
        print("April fool day already went by %d days ago" % ((today-afd).days))
        afd = afd.replace(year=today.year+1)
    time_to_afd= afd-today
    print("its just ", time_to_afd , "days untill next afd")
if __name__=="__main__":
    main()


