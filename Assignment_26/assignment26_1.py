class Demo:
    value = 0
    def __init__(self, no1,no2):
        self.no1 = no1
        self.no2=no2
    


    def fun(self):
        a = self.no1
        b = self.no2
        print("value from the method fun : ",a)
        print("Value from the method fun : ",b)

    def gun(self):
       a = self.no1
       b = self.no2
       print("value from the method gun : ",a)
       print("Value from the method gun : ",b)
       

obj1 = Demo(11,21)
obj2 = Demo(50,60)

obj1.gun()
obj1.fun()

obj2.gun()
obj2.fun()
        


        