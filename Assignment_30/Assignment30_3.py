import datetime
import time 
import schedule


def display():

    print("CODING KARR......!")

def main():
    schedule.every(30).minutes.do(display)


    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()