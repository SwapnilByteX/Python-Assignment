divisible = lambda no: no % 5 == 0 

def main():
    print("enter one number:")
    v1 = int(input())
    ret = divisible(v1)
    print(ret)

if __name__ == "__main__":
    main()