def divide(no):
    if (no%3==0 and no%5==0):
        print("enterred number is divisible")
    else:
        print("not divisible")



def main():
    print("enter one number:")
    v1 = int(input())

    ret = divide(v1)
    print(ret)



if __name__ == "__main__":
    main()