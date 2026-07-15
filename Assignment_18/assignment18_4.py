def main():
    no = int(input("enter size of list"))
    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    print(data)
    
    num = int(input("enter any number from list"))
    count = 0

    for i in data:
        if i == num:
            count += 1
        
    print(count)
if  __name__ == "__main__":
    main()