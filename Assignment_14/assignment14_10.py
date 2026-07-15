
largest = lambda no1, no2, no3 : no1 if no1 > no2 and no1 > no3 else no2 if no2 > no3 and no2 > no1 else no3
def main():
    print("enter first number")
    v1 = int(input())

    print("enter first number")
    v2 = int(input())

    print("enter first number")
    v3 = int(input())

    ret = largest(v1,v2,v3)
    print(ret)


if __name__ == "__main__":
    main()