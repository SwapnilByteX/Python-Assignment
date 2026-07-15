import multiprocessing
def prime(no):
    total = 0
    sum = 0
    res = []
    for no in range(2,no +1):
        count = 0
        for i in range(1,no + 1):
            if no % i == 0:
                count = count + 1

        if count == 2:
            total = total + 1
    print("total count is :",total)
        


def main():
    data = [100,200,300,400]
    
    pobj = multiprocessing.Pool()

    res = pobj.map(prime,data)
    





if __name__ =="__main__":
    main()