def posneg(no):
    if (no>0):
        print("number is positive")

    else:
        print("number is negavtive")

def main():

    print("enter any number : ")
    v1 = int(input())

    ret = posneg(v1)
    print(ret)

if __name__ == "__main__":
    main()