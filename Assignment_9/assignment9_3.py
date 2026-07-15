def square(no):
    ans = no * no
    return ans

def main():
    print("enter one number :")
    v1 = int(input())

    res = square(v1)
    print("Square of given no is : ",res)


if __name__ == "__main__":
    main()
