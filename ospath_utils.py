import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    print("Item exists: "+ str(path.exists("file_handling.py")))
    print("Item is a file: "+ str(path.isfile("D:/")))
    print("Item is a file: "+ str(path.isfile("file_handling.py")))
    print("Item is a Directory: "+ str(path.isdir("file_handling.py")))
    print("Item is a Directory: "+ str(path.isdir("D:/")))
    print("Item's Real path: "+ str(path.realpath("file_handling.py")))
    print("Item's path and name: "+ str(path.split(path.realpath("file_handling.py"))))
    t = time.ctime(path.getmtime("file_handling.py"))
    print("file modification time:" + t)
    print(path.getsize("file_handling.py") )
    print(datetime.datetime.fromtimestamp(path.getmtime("file_handling.py")))
    td = datetime.datetime.now()- datetime.datetime.fromtimestamp(path.getmtime("file_handling.py"))
    print("file was modified " + str(td) + " ago")
    
if __name__=="__main__":
       main()
      
