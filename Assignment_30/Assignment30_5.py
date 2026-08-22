import time 
import schedule
import datetime

def display():
    

    fobj = open("Marvellous.txt",'a')

    fobj.write(str(datetime.datetime.now()) + "\n")

    print("Data Written Sucessfully")


def main():
    schedule.every(5).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()