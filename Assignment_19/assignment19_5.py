from functools import reduce
def filterr(no):
    count = 0
    for i in range(1, no + 1):
        if no % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False
                

addition = lambda no1,no2: no1 if no1>no2 else no2

maap = lambda no1: no1 * 2

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


