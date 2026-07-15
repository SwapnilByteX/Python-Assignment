from functools import reduce
def addition(no1,no2): 
    return no1 + no2


def main():

    no = int(input("enter any number"))
    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    print(data)

    rdata = reduce(addition,data)
    print(rdata)



if __name__ == "__main__":
    main()