import threading
def even():
    for i in range(2,20+2):
        if i % 2 == 0:
            
            print(i)
    print()


def odd():
    for i in range(1,20+1):
        if i % 2 != 0:
            
            print(i)
    


def main():
    
    t1 = threading.Thread(target=even)
    t2 = threading.Thread(target=odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    
    


if __name__=="__main__":
    main()


