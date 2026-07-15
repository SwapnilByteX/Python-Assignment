chkgreater = lambda no1, no2 : no1> no2

def main():
    print("enter first number:")
    v1= int(input())

    print("enter second number:")
    v2 = int(input())


    ret = chkgreater(v1,v2)
    if ret == True:
        print(f"{v1} is greater")

    else:
        print(f"{v2} is greater")
        


if __name__ == "__main__":
    main()