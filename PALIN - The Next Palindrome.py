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

if len(numbers)%2==0:
    pass

k = "657576"
def check(number):
    for i in range((len(k)/2)+1):
        if k[i]==k[-i-1]:
            print "TAKA SAMA LICZBA NA %s pozycji oraz automatycznie na %s"%((int(i)+1),(len(k)-i))

        else:
            k[-i]=int(k[-i])+1
    check(number)
    print number

check("3333")
#ask_for_INPUT()
print numbers