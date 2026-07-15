def main():
    no = int(input("enter any number : "))
    count = 0    
    for i in range(1,no + 1):
        if no % i == 0:
            count += 1

    if (count == 2):
        print("number is prime ")

    else:
        print("number is not prime")

if __name__ == "__main__":
    main()
 