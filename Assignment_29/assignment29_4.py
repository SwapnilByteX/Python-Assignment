import os
def main():
    res = input()
    ret = os.path.exists(res)
    a = open(res,"r")
    data = a.read()

    res1 = input()
    ret1 = os.path.exists(res1)
    a1 = open(res1,"r")
    data1 = a1.read()

    if data == data1:
        print("same content")
        
    else:
        print("No content match")

        
if __name__ == "__main__":
    main()