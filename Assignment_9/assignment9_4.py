def Cube(no):
    ans = no * no * no
    return ans

def main():
    print("enter one number :")
    v1 = int(input())

    res = Cube(v1)
    print("Cube of given no is : ",res)


if __name__ == "__main__":
    main()
