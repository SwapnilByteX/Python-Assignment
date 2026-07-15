
def main():
    no = int(input("Enter no"))

    
    sum = 0
    for i in range(1,no + 1):
        if (no % i == 0 ):
            print(i)
            sum = sum + i
    print(sum)

       
        

if __name__ == "__main__":
    main()