import multiprocessing
def odd(no):
    total = 0
    for i in range(1,no + 1):
        if (i % 2 != 0):
            total = total + i
    print("total count of odd : ",total)




def main():
    data = [100,200,300,400]

    oobj = multiprocessing.Pool()

    res = oobj.map(odd,data)

    print(res)

    oobj.close()
    oobj.join()


if __name__=="__main__":
    main()