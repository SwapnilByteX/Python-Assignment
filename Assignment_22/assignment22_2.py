import multiprocessing
def square(no):
    fact = 1
    for i in range(1,no +1):
        fact = fact * i

       
    print("factorial of number :",fact)


def main():
    data = [5,15,20,25]
    

    sobj = multiprocessing.Pool()

    res = sobj.map(square,data)

    sobj.close()
    sobj.join()
    

   


if __name__=="__main__":
    main()