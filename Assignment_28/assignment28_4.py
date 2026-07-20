def main():
    filename = input()
    fobj = open(filename,"r")
    data = fobj.read()

    filename2 = input()
    fobj2 = open(filename2,"w")
    


    
    print("Content of file : ",data)

    a = fobj2.write(data)
    print("data return successfully in second file")

    fobj.close()
    



if __name__=="__main__":
    main()