
from datetime import date
from datetime import time
from datetime import datetime

def main():
    today =datetime.now()
    print("current date is:", today)
    t= datetime.time(datetime.now())
    print("current time is: ", t)

if __name__=="__main__":
    main()
