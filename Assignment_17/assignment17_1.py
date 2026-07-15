def add(no1, no2):
    return no1 + no2

def sub(no1,no2):
    return  no1 - no2

def mul(no1,no2):
    return no1 * no2

def div(no1,no2):
    return no1 / no2

def main():
    print("Enter first number")
    v1 = int(input())

    print("Enter Second number")
    v2 = int(input())

    print("addition is : ",add(v1,v2))
    
    print("substraction is :",sub(v1,v2)) 
    
    print("multiplication is :",mul(v1,v2))
    
    print("Division is :",div(v1,v2))
    
    

if __name__ == "__main__":
    main()
