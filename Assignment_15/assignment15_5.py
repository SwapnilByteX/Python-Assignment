from functools import reduce

maximun = lambda no1,no2 : no1 if no1>no2 else no2

def main():
    Data = list() 
    no = int(input("Enter a number : "))
    for i in range(no):
        value = int(input("Enter a value : "))
        Data.append(value)

    ret = reduce(maximun, Data)

    print("Maximum no from list is : ",ret)

    


if __name__ == "__main__":
    main()