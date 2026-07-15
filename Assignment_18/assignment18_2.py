from functools import reduce
maximum = lambda no1,no2: no1 if no1 > no2 else no2
    

def main():
    no = int(input("enter size of list"))
    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    print (data)

    ret = reduce(maximum,data)
    print(ret)


if __name__ == "__main__":
    main()