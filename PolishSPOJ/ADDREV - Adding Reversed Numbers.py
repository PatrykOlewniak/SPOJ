#http://www.spoj.com/problems/ADDREV/
"""
[Input]The input consists of N cases (equal to about 10000).
The first line of the input contains only positive integer N.
Then follow the cases. Each case consists of exactly one line
with two positive integers separated by space. These are the reversed
numbers you are to add.

[Output]
For each case, print exactly one line containing only one integer
 - the reversed sum of two reversed numbers.
  Omit any leading zeros in the output.
"""

#we could use reverse function but not so easy this time :)


listOfNumbers = []


def reverseNumber(number):
    try:
        number = str(number)[::-1]
        return int(number)
    except:
        print ("Not a number on input")


def getNumbers():
    amountOfNumbers = int(raw_input())
    while amountOfNumbers:
        number1, number2 = (raw_input().split(" "))
        listOfNumbers.append([number1,number2])
        amountOfNumbers=amountOfNumbers-1


def reverseSum(number1,number2):
    return reverseNumber(number1) + reverseNumber(number2)


def calculate(listOfNumbers):
    for numbers in listOfNumbers:
        print reverseNumber(reverseSum(int(numbers[0]),int(numbers[1])))


if __name__ == '__main__':
    getNumbers()
    calculate(listOfNumbers)