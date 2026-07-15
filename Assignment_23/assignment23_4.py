import multiprocessing
import os
def odd(no):
    count = 0
    for i in range(1, no + 1):
        if i % 2 !=0:
            count = count + 1
    print("count of total odd number : ",count)



def main():
    data = [100,200,300,400]

    oobj = multiprocessing.Pool()
    res = oobj.map(odd,data)

    oobj.close()
    oobj.join()
    print("process id : ",os.getpid())
    print("process id : ",os.getppid())


if __name__=="__main__":
    main()