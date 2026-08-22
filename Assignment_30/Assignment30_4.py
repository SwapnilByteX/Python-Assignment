import schedule 
import time
import datetime



def display():

    print("Namaskaar Mandali...!")

def main():
    schedule.every().days.at("09:00").do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()