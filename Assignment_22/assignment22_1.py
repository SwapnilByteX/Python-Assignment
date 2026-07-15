import multiprocessing
def square(no):
    sum = 0
    for i in range(1,no +1):
        
        s = i*i
        print(s)
    sum = sum + s
    print("sum of square",sum)


def main():
    data = [100,200,300,400]
    res =[]

    sobj = multiprocessing.Pool()

    res = sobj.map(square,data)

    sobj.close()
    sobj.join()
    

    print("Result is ",res)


if __name__=="__main__":
    main()