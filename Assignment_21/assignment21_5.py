import threading
sumr = 0
product1 = 1

def add():
    global sumr 
    sumr = sum(data)

def product():
    global product1 
    for i in data:
        product1 = product1 * i
        
no = int(input("enter size of list"))
data = []
for i in range(no):
    x = int(input())
    data.append(x)
print(data)

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=product)

t1.start()
t2.start()

t1.join()
t2.join()

print("sum = ",sumr)
print("sum = ",product1)




