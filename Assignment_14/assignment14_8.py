addition = lambda no1, no2 : no1 + no2

def main():
    print("enter first number")
    v1 = int(input())

    print("enter second number")
    v2 = int(input())

    ret = addition(v1,v2)
    print(ret)

if __name__ == "__main__":
    main()

