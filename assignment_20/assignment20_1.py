import time
import threading

def sumeven(no):
    sum = 0

    for i in range(2,no,2):
        sum = sum+i
    print("summation of even",sum)

def sumodd(no):
     sum = 0

     for i in range(1,no,2):
        sum = sum+i
     print("summation of odd",sum)



def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=sumeven, args=(100000))
    t2 = threading.Thread(target=sumodd, args=(100000))
    t1.start()
    t2.start()
    end_time = time.perf_counter()
    print(f"time required :{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()