import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("file_handling.py"):
        src = path.realpath("file_handling.py")
        dst = src + ".txt"
        shutil.copy(src, dst)
        print("does new file exist?: " + str(path.exists(dst)))
        #rename file
        os.rename("file_handling.py.txt", "newfile.doc")
        
if __name__=="__main__":
       main()
      
