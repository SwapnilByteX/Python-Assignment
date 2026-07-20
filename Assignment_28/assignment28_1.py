def main():
    filename = input()
    count = 0
    fobj = open(filename,"r")

    for i in fobj:
        count = count + 1
    print("number of line",count)




if __name__=="__main__":
    main()