#http://www.spoj.com/problems/PIGBANK/
"""
[Input]The input consists of T test cases. The number of them (T) is given on the first line of the input file.
Each test case begins with a line containing two integers E and F.
They indicate the weight of an empty pig and of the pig filled with coins.
Both weights are given in grams. No pig will weigh more than 10 kg, that means 1 <= E <= F <= 10000.
On the second line of each test case, there is an integer number N (1 <= N <= 500) that gives the number of various coins
used in the given currency. Following this are exactly N lines, each specifying one coin type.
These lines contain two integers each, P and W (1 <= P <= 50000, 1 <= W <=10000). P is the value of the coin in monetary units,
W is it's weight in grams.

[Output]Print exactly one line of output for each test case.
The line must contain the sentence "The minimum amount of money in the piggy-bank is X."
where X is the minimum amount of money that can be achieved using coins with the given total weight.
If the weight cannot be reached exactly, print a line "This is impossible.".
"""

coinsAndWeight = []


def ask_for_INPUT():
    numberOfTests = raw_input()
    for numberOfTest in range(int(numberOfTests)):
        caseList=[]
        newValue = raw_input()
        caseList.append(newValue.split(" "))
        differentCoinsAmount = int(raw_input())
        caseList.append(coins((differentCoinsAmount)))
        coinsAndWeight.append(caseList)



def coins(numberOfVariousCoins):
    coins={}
    for k in range(numberOfVariousCoins):
        newCoin = raw_input()
        m,n=(newCoin.split(" "))
        coins[m]=n
    return coins

def get_weight_of_PiggyBank(subList):
    return int(subList[0][1]) - int(subList[0][0])


#ask_for_INPUT()

def calculate_the_Coins(subList):
    totalMoney=0
    totalWeight = get_weight_of_PiggyBank(subList)



for k in range(len(coinsAndWeight)):
    print get_weight_of_PiggyBank(coinsAndWeight[k])
print coinsAndWeight
print get_weight_of_PiggyBank(coinsAndWeight[2])


def coins(times,value,key):
    pass