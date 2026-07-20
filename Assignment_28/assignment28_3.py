def main():
    filename = input()

    fobj = open(filename,"r")
    data = fobj.read()
    
    print("Content of file : ",data)
    fobj.close()
    



if __name__=="__main__":
    main()