
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
