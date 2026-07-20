def main():
    filename = input()
   
    fobj = open(filename,"r")
    data = fobj.read()
    word = data.split()

    print("total count of word :",len(word))

    fobj.close()
    



if __name__=="__main__":
    main()