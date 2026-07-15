chkevenodd = lambda no1 : no1 % 2 != 0

def main():
    print("enter first number:")
    v1= int(input())

    ret = chkevenodd(v1)
    print(ret)
        


if __name__ == "__main__":
    main()  