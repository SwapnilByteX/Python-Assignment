import multiprocessing
def even(no):
    count = 0
    for i in range(2,no +1):
        if i % 2 ==0:
            count = count + 1
    print("count of even no :",count)


def main():
    data = [100,200,300,400]

    eobj = multiprocessing.Pool()
    res = eobj.map(even,data)
    


if __name__=="__main__":
    main()