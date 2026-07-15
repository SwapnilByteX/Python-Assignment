import time
import multiprocessing
def square(no):
    
    for i in range(1,no +1):
        fact = i**5

       
    print("factorial of number :",fact)


def main():
    data = [1000000,2000000,300000,400000]

    starttime = time.perf_counter()
    
    

    sobj = multiprocessing.Pool()

    res = sobj.map(square,data)

    sobj.close()
    sobj.join()
    
    endtime = time.perf_counter()

    totaltime = starttime - endtime
    print("total time required is :",totaltime)

   


if __name__=="__main__":
    main()