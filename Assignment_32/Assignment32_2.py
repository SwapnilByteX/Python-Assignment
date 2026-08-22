import os
import schedule
import time
import datetime


def filesize(filepath):

    if not os.path.isfile(filepath):
        print("file does not exist")
        return

    size = os.path.getsize(filepath)

    fobj = open("filesizelog.txt",'a')
    fobj.write(f"File path : {filepath} \n")
    fobj.write(f"File size : {size} \n")
    fobj.write(f"Date and time : {datetime.datetime.now()} \n")

    print("Data Written Sucessfully")

    fobj.close()


def main():
    filepath = input("enter file path :")

    schedule.every(30).seconds.do(filesize,filepath)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()
