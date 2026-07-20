import os


def main():
    res = input()
    ret = os.path.exists(res)
    a = open(res,"r")
    data = a.read()

    if ret == True:
        print("file is present")
        print(data)

    else:
        print("there is no such file")


    b = open("abc.txt","w")
    data1 = b.write(data)

    print("Content Written Successfully")
    
        
if __name__ == "__main__":
    main()