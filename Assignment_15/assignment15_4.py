from functools import reduce
addition = lambda no1,no2: no1 + no2


def main():
    data = [10,11,12,13,14,15]
    print("list of number :",data)

    rdata = reduce(addition,data)
    print("aditions of number:",rdata)



if __name__ == "__main__":
    main()