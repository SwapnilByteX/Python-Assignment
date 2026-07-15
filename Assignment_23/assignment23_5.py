import multiprocessing
def factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact*i
    print("factorial of number : ",fact)

def main():
    data = [10,40,30,20]

    fobj = multiprocessing.Pool()

    res = fobj.map(factorial,data)

    fobj.close()
    fobj.join()



if __name__=="__main__":
    main()