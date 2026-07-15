def main():
    no = int(input("Enter any number"))
    sum = 0

   

    while 0 < no:
        lst  = no % 10
        sum = sum + lst
        no = no // 10
    print(sum)

    

if __name__ == "__main__":
    main()