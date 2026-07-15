def square(no):
    return no * no
    
def main():
    Data = [13,12,8,10,11,20]
    print("input data is :",Data)

   

    MData = list(map(square,Data))
    print("data after map:",MData)

   

    

if __name__ == "__main__":
    main()

     