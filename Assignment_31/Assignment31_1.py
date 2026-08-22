import schedule
import time
import datetime




def display(A):
    print(A)
def main():
    
    n = int(input("Enter Seconds : "))
    A = input("Enter Any Message : ")
    schedule.every(n).seconds.do(display,A)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()