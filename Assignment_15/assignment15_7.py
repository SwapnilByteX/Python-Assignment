str = lambda no: len(no)>=5 

def main():
    data = []
    no = int(input("enter size of list"))

    for i in range(no):
        x = input()
        data.append(x)
    print("list of string",data)

    fdata = list(filter(str,data))
    print(fdata)


if __name__ == "__main__":
    main()
    