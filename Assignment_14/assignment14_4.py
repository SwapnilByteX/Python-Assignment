chksmaller = lambda no1, no2 : no1> no2

def main():
    print("enter first number:")
    v1= int(input())

    print("enter second number:")
    v2 = int(input())


    ret = chksmaller(v1,v2)
    if ret == False:
        print(f"{v1} is smaller")

    else:
        print(f"{v2} is smaller")
        


if __name__ == "__main__":
    main()