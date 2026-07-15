odd = lambda no : no % 2 != 0

def main():
    data = [10,11,12,13,14,15,16]
    print(" list of number  :", data)

    fdata = list(filter(odd,data))
    print("data after filter:",fdata)

if __name__ == "__main__":
    main()
    