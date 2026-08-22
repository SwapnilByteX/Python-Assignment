import time 
import schedule
import datetime

def displayMessage(Message):
    print(Message)


def main():
    Message = input("Enter Any Message : ")

    schedule.every(5).seconds.do(displayMessage,Message)

    while True:
        schedule.run_pending()
        time.sleep(1)
 

if __name__ == "__main__":
    main()