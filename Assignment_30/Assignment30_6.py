import datetime
import time
import schedule


def lunch():
    print("Its Lunch Time....!")


def end():
    print("Wrap up Work...!")


def main():
    schedule.every().days.at("13:00").do(lunch)

    schedule.every().days.at("18:00").do(end)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()