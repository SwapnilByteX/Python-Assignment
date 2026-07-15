def main():
    no = int(input("Enter any number"))
    sum = 0

    count = 0
    while (0<no):
        no = no // 10
        count = count + 1
    print(count)

    

if __name__ == "__main__":
    main()