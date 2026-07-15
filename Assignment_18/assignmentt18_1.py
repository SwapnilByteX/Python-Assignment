def Addition(data):

    sum = 0
    for i in data:
        sum = sum + i
    return sum

def main():
    no = int(input("enter number"))

    data = []
    for i in range(no):
        x = int(input())
        data.append(x)
    print(data)

    ret = Addition(data)
    print(ret)


if __name__ == "__main__":
    main()