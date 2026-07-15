def divisible(no):
    if (no % 5 == 0 ) :
        print("number is divisible")
    else:
        print("not divisible")


def main():
    print("Enter the number")
    v1 = int(input())

    ret = divisible(v1)
    print(ret)

if __name__ == "__main__":
    main()