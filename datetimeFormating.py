
from datetime import datetime

def main():
    now =datetime.now()
# %y/%Y--Year , %a/%A--Weekday , %b/%B--month , %d--day of month    
    print(now.strftime("the current year is: %Y %y"))
    print(now.strftime("the current weekday is: %A %a"))
    print(now.strftime("the current month is: %B %b"))
    print(now.strftime("the current date is: %D %d"))    
    print(now.strftime("%A %B %D"))
    print(now.strftime("%a, %b %d, %Y"))
# %c- locale's date and time, %x- locale's date, %x-locale's time    
    print(now.strftime("locale date and time: %c"))
    print(now.strftime("locale date: %x"))
    print(now.strftime("locale time: %X"))
# %I/%H - 12/24 hour, %M- minute, %S-second, %p-locale's AM/PM 
    print(now.strftime("current time: %I:%M:%S %p"))
    print(now.strftime("24 hr current time: %H:%M:%S"))
if __name__=="__main__":
    main()


