import threading
def number():
    print("Number from 1 to 50")
    for i in range(1,50 + 1):
        print(i)
    print()

def reverse():
    print("Reverse number")
    for i in range(50,0,-1):
        print(i)


def main():
    t1 = threading.Thread(target=number)
    t2 = threading.Thread(target=reverse)

    t1.start()
    t1.join()

    t2.start()
    t2.join()



if __name__=="__main__":
    main()