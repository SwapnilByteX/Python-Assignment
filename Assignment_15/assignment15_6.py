from functools import reduce 
minimum = lambda no1, no2 : no1 if no1< no2 else no1


def main():
    data = []
    no = int(input("enter size of list"))
    for i in range(no):
        x = int(input())
        data.append(x)
    print("list element",data)

    rdata = reduce(minimum,data)
    print(rdata)



if __name__ == "__main__":
    main()