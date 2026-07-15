from functools import reduce
product = lambda no1,  no2 : no1 * no2

def main():
    data = []
    no = int(input("number of element"))
     
    for i in range(no):
        x = int(input())
        data.append(x)

    rdata = reduce(product,data)
    print(rdata)


if __name__ == "__main__":
    main()