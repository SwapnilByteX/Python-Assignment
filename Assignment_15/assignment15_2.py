even = lambda no: no % 2 == 0

def main():

    data = [10,11,12,13,14,15]
    print("number of list is :",data)

    fdata = list(filter(even,data))
    print("number of list after filter:",fdata)


if __name__ == "__main__":
    main()