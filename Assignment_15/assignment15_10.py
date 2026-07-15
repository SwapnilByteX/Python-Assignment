evencount = lambda no :  (no % 2==0 )

def main():
    count = 0
    
    data = []
    no = int(input("enter size of list"))

    for i in range(no):
        x = int(input())
        data.append(x)

    print("list of number ",data)

    fdata = list(filter(evencount,data))
    print(fdata)

    for i in fdata:
        count = count + 1

    print(count)
    


if __name__ == "__main__":
    main()

