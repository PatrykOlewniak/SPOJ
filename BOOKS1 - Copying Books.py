# http://www.spoj.com/problems/BOOKS1/
"""
[Input]The input consists of N cases (equal to about 200).
The first line of the input contains only positive integer N.
Then follow the cases. Each case consists of exactly two lines.
At the first line, there are two integers m and k, 1 <= k <= m <= 500.
At the second line, there are integers p1, p2, ... pm separated by spaces.
All these values are positive and less than 10000000.

[Output]For each case, print exactly one line.
The line must contain the input succession p1, p2, ... pm divided
into exactly k parts such that the maximum sum of a single part
should be as small as possible. Use the slash character ('/') to separate the parts.
There must be exactly one space character between any two successive
numbers and between the number and the slash.

If there is more than one solution, print the one that minimizes the
work assigned to the first scriber, then to the second scriber etc.
But each scriber must be assigned at least one book.

Sample input:
2
9 3
100 200 300 400 500 600 700 800 900
5 4
100 100 100 100 100

Sample output:
100 200 300 400 500 / 600 700 / 800 900
100 / 100 / 100 / 100 100

"""
#[[scribers],[parts]]
mainList = []


def getValues(listToAddNewValues):
    amountOfNumbers = int(raw_input())
    for k in range(0,amountOfNumbers):
        parts, scribers = raw_input().split(" ")
        parts = raw_input().split(" ")
        listToAddNewValues.append([scribers, parts])


testList = [['4', "100 100 100 100 100"]]


def sumOfElements(listOfStrElements):
    summ = 0
    if type(listOfStrElements) is str:
        tempList=listOfStrElements.split(" ")
        for number in tempList:
            summ += int(number)
        return summ
    else:
        return -1


def averageValueOfElements(listOfNumbers):
    if type(listOfNumbers) == str:
        return (sumOfElements(listOfNumbers)) / len(listOfNumbers.split(" "))
    else:
        return 0


#draft
def splitBetweenScribers(inputList):
    totalPages = sumOfElements(inputList[1])
    average = averageValueOfElements(inputList[1])
    scribersAmount = int(inputList[0])
    listOfNumbers = inputList[1].split(" ")
    amountOfNumbers = len(listOfNumbers)
    tempList1=listOfNumbers

    elementsSum = 0
    indexesOfBackslash=[]
    for i in range(0,amountOfNumbers):

        elementsSum += int(listOfNumbers[i])
        if elementsSum > (totalPages/scribersAmount):
            elementsSum = 0
            indexesOfBackslash.append(i)
    while indexesOfBackslash:
        tempList1.insert(indexesOfBackslash.pop(), r"/")
    return tempList1


def tests():
    print type(testList[0][1])
    print averageValueOfElements(testList[0][1])
    print sumOfElements(testList[0][1])
    #getValues(mainList)
    #print mainList
    print splitBetweenScribers(testList[0])





if __name__ == "__main__":
    tests()
