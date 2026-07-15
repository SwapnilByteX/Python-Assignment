from functools import reduce
import threading
maximum = lambda no1, no2 : no1 if no1 > no2 else no2
    
minimum = lambda no1, no2 : no1 if no1 < no2 else no2

def maximumX(data):
    ret = reduce(maximum,data)
    print("the maximum number",ret)

def minimumX(data):
    ret = reduce(minimum,data)
    print("the minimum number",ret)

def main():
    no = int(input("Size of list"))
    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    
    t1 = threading.Thread(target=maximumX,args=(data,))
    t2 = threading.Thread(target=minimumX,args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()



if __name__=="__main__":
    main()