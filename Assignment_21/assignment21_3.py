import threading
def prime(Data):
    Prime = []
    for No in Data:
        if No <= 1:
            continue
        for i in range(2,No) :
            if No % i == 0:
                break
        else:
            Prime.append(No)

    print(Prime)

def NonPrime(Data):
    Non_Prime = []

    for No in Data:
        if No <= 1:
            Non_Prime.append(No)
            continue
        
        for i in range(2,No) :
            if No % i == 0:
                Non_Prime.append(No)
                break

    print(Non_Prime)

def main():
    no = int(input("Size of list"))
    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    
    t1 = threading.Thread(target=prime,args=(data,))
    t2 = threading.Thread(target=NonPrime,args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()



if __name__=="__main__":
    main()