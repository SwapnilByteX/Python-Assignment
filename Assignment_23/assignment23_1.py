import multiprocessing
import os

def even(no):
    total = 0
    
    for i in range(1,no +1):
        
        if (i % 2 == 0):
            
            total = total + i
    print("sum of even",total)


def main():
    data = [100,200,300,400]
    res =[]

    sobj = multiprocessing.Pool()

    res = sobj.map(even,data)
    

    print("Result is ",res)

    print("process ID :",os.getpid())
    print("process ID :",os.getppid())


if __name__=="__main__":
    main()