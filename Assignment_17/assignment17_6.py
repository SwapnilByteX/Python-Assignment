def main():
    no = int(input("enter any number :"))

    fact = 1

    for i in range(1, no + 1):
        fact = fact * i
    
    print("Factorial of number is : ",fact)
  
 
if __name__ == "__main__":
    main()