import threading 
def evenfactor(no):
    sum = 0
    for i in range(2,no + 1):
        if no % i == 0 and i % 2 == 0:
            print("even",i)
            sum = sum + 1
            print("sum of even number",sum)
    


def oddfactor(no):
    sum = 0
    for i in range(1,no + 1):
        if no % i == 0 and i % 2 != 0:
            
            print("odd",i)
        
            sum = sum +i
            print("sum of odd number",sum)
    


def main():
    print("enter any number")
    no = int(input())
    
    t1 = threading.Thread(target=evenfactor,args=(no,))
    t2 = threading.Thread(target=oddfactor,args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("exit from main")
    
    


if __name__=="__main__":
    main()


