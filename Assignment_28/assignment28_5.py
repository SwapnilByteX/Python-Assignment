def main():
    filename = input("Enter file name : ")
    word = input("enter the word to search : ")
    fobj = open(filename,"r")
    data = fobj.read()
                                   


    if word in data:
        print("word is present")

    else:
        print("word is not present")



if __name__=="__main__":
    main()