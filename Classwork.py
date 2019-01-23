def main():
    # prob1()
    # prob2()
    # prob3()
    # prob4()
    prob5()


def prob1():
    myList = ["Kenn", "Kevin", "Erin", "Meka"]
    print(myList[2])
    print(len(myList))
    myList.pop(2)
    print(myList[2])

def prob2():
    while 1 == 1:
        Word = input("Enter a word")
        if Word == "q":
            break

def prob3():
    newList = {
        "Jonathan": "John",
        "Michael": "Mike",
        "William": "Bill",
        "Robert": "Rob"
    }
    print(newList)
    print(newList["William"])


def prob4():
    numList = [42, 654, 2, 82, 13421]
    numList.reverse()
    print(numList)


def prob5():
    highList = [324, 12, 34, 2, 4, 52, 64, 865, 23, 3, 435, 87676, 0]
    x = 1
    tEqual = 0
    tLower = 0
    tHigher = 0
    userNum = int(input("Enter a number: "))
    while x <= len(highList):
        if userNum == int(highList[x - 1]):
            tEqual += 1
            x += 1
        elif userNum > int(highList[x - 1]):
            tHigher += 1
            x += 1
        elif userNum < int(highList[x - 1]):
            tLower += 1
            x += 1
        else:
            print("Error")
            break

    print("There are", tLower, "numbers lower,", tHigher, "numbers higher, and", tEqual, "numbers equal to", userNum)


if __name__ == '__main__':
    main()
