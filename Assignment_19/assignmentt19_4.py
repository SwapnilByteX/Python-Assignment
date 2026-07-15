from functools import reduce
filterr = lambda no : no % 2 == 0
        

addition = lambda no1,no2: no1 + no2

maap = lambda no1: no1 ** 2

def main():
    no = int(input("Enter size of list : "))
    data = []

    for i in range(no):
        x = int(input())
        data.append(x)
    print("the list data",data)

    fdata = list(filter(filterr,data))
    print("after filter : ",fdata)

    mdata = list(map(maap,fdata))
    print("after map",mdata)

    rdata = reduce(addition,mdata)
    print("after reduce",rdata)


if __name__ == "__main__":
    main()


