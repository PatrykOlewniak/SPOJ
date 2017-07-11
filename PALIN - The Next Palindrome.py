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
    amountOfPalindromes= raw_input()
    for number in range(int(amountOfPalindromes)):
        newValue = (raw_input())
        numbers.append(newValue)

def isPalindrome(number):
    pass

def number_to_list(number):
    return list(str(number))

def palindrome_maker(listOfNumbers):
    listLength = len(listOfNumbers)
    if not isPalindrome(listOfNumbers):
        if listLength%2==0:
            for k in range((len(listOfNumbers)/2)):
                if listOfNumbers[k]!=listOfNumbers[-k-1]:
                    if listOfNumbers[-k-1]==int(9):
                        listOfNumbers[-k-1]=str(0)
                        listOfNumbers[-k - 2] =str(int(listOfNumbers[-k - 2]))+1
                        palindrome_maker(listOfNumbers)
                    else:
                        listOfNumbers[-k - 1] = str(int(listOfNumbers[-k - 1]) + 1)
                        palindrome_maker(listOfNumbers)


    return listOfNumbers

def get_the_lowest_next_palindrome(number):
    number = number_to_list(number)
    palindrome_maker(number)
    return number

def isPalindrome(number):
    tempList=number_to_list(number)
    for k in range((len(tempList)/2)+1):
        if tempList[k]!=tempList[-k-1]:
            return False
    return True


k=8221
print palindrome_maker(number_to_list(4123))