divisible = lambda no : no % 3 == 0 and no % 5 == 0

def main():
    data = []
    no = int(input("enter list size"))
    
    for i in range(no):
        x = int(input())
        data.append(x)
    print("list of number",data)

    fdata = list(filter(divisible,data))
    print(fdata)

if __name__ == "__main__":
    main()