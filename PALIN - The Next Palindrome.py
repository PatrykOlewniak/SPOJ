"""
A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left.
 For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output.
 Numbers are always displayed without leading zeros.

[Input]he first line contains integer t, the number of test cases. Integers K are given in the next t lines.
[Output] For each K, output the smallest palindrome larger than K.

Example:
Input:
2
808
2133

Output:
818
2222
"""

numbers = []

def ask_for_INPUT():
    amountOfPalindromes= input()
    for number in range(int(amountOfPalindromes)):
        newValue = input()
        numbers.append(int(newValue))

def number_to_list(number):
    return list(str(number))


def isPalindrome(number):
    tempList=number_to_list(number)
    for k in range(int(len(tempList)/2)+1):
        if tempList[k]!=tempList[-k-1]:
            return False
    return True

def palindrome_from_number(number):
    number = number+1
    while not(isPalindrome(number)):
        number=number+1
    return number

ask_for_INPUT()
for i in numbers:
    print (palindrome_from_number(i))

