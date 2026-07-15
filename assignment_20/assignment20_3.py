import threading 
def evenfactor(data):
    sum = 0
    for i in data:
        if  i % 2 == 0:
            print(i)
            sum = sum + i
            print("sum of number",sum)
    


def oddfactor(data):
    sum = 0
    for i in data:
        if  i % 2 != 0:
            
            print(i)
        
            #sum = sum +1
            #print("sum of number",sum)
    


def main():
    print("enter any number")
    no = int(input())
    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    print(data)


    
    t1 = threading.Thread(target=evenfactor,args=(data,))
    t2 = threading.Thread(target=oddfactor,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    
    


if __name__=="__main__":
    main()


