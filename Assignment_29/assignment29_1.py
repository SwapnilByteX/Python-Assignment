import os


def main():
    res = input()
    ret = os.path.exists(res)

    if ret == True:
        print("file is present")
        

    else:
        print("there is no such file")
        
if __name__ == "__main__":
    main()