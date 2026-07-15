def chkgreater(no1, no2):
    if (no1 > no2):
        print("first no is greater",no1)
    else:
        print("second no is greater",no2)
     

def main():
    print("enter first number")
    v1 = int(input())

    print("enter second number")

    v2 = int(input())

    res = chkgreater(v1, v2)

if __name__ == "__main__":
    main()

