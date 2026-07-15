import threading

def small(str):
    count = 0
    for i in str:
        if i.islower():
            print(i)
            count = count + 1
    print("count of lower is :",count)
    print("thread id is",threading.get_ident())


def capital(str):
    count = 0
    for i in str:
        if i.isupper():
            print(i)
            count = count + 1
    print("count of upper is",count)
    print("thread id is ",threading.get_ident())

def digits(str):
    count = 0
    for i in str:
        if i.isdigit():
            print(i)
            count = count + 1
    print("number of digit :",count)
    print("thread id is :",threading.get_ident())

def main():
    print("enter any string : ")
    str = input()

    t1 = threading.Thread(target=small,args=(str,))
    t2 = threading.Thread(target=capital,args=(str,))
    t3 = threading.Thread(target=digits,args=(str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__=="__main__":
    main()