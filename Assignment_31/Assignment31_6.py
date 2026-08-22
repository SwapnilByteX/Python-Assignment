import schedule
import time
import datetime

def monday():
    print("Start Your weekly goal")

def Wednesday():
    print("Review your Weekly Progress")

def friday():
    print("Weekly Progress completed")

def main():
    schedule.every().monday.at("09:00").do(monday)
    schedule.every().wednesday.at("17:00").do(Wednesday)
    schedule.every().friday.at("18:00").do(friday)


    while True:
        schedule.run_pending()
        time.sleep(1)
 

if __name__ == "__main__":
    main()