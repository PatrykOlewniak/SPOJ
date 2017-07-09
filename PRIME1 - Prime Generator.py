"""
Peter wants to generate some prime numbers for his cryptosystem. Help him!
Your task is to generate all prime numbers between two given numbers!

[Input]The input begins with the number t of test cases in a single line (t<=10).
In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

[Output]For every test case print all prime numbers p such that m <= p <= n, one number per line,
test cases separated by an empty line.


"""



numbers = []

def ask_for_INPUT():
    amountOfNubers = raw_input()
    for number in range(int(amountOfNubers)):
        newValue = raw_input()
        numbers.append(newValue)

def is_Prime(number):
    if number <= 1:
        return False

    for k in range(2, (number / 2) + 1):
        if number % k == 0:
            return False
    else:
        return True

def list_is_Prime_check(listOfInputNumbers):
    for k in listOfInputNumbers:
        kTemp = k.split(" ")
        for i in range(int(kTemp[0]), int(kTemp[1])):
            if is_Prime(i):
                print i
        print ""  # for right output separated with empty line

ask_for_INPUT()
list_is_Prime_check(numbers)
