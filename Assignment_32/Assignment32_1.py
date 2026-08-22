import time
import schedule
import datetime

def display():
    CurrentTime = datetime.datetime.now()
    Filename = f"File_{CurrentTime}.txt"

    fobj = open(Filename,"w")

    fobj.write(f"File Name : {Filename}\n")
    fobj.write(f"Creation Date :  {datetime.date.today()} \n")
    fobj.write(f"Creation Time : {datetime.datetime.now()}")

    fobj.close()

    print("File Sucessfully Created ")
   


def main():

    schedule.every(1).seconds.do(display)


    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()