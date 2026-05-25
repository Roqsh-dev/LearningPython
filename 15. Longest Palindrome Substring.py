

def isPalindrome(string):
    digitList = []

    for digit in string:
        digitList.append(digit)

    reversedString = ""
    for i in range(len(digitList) - 1, -1, -1):
        reversedString += digitList[i]

    return string == reversedString

def longestPalindrome(string):
    if string == "":
        return ""
    
    potentialPals = []

    for i in range(len(string)):
        substring = ""

        for s in string[(i):]:
            substring += s

            if isPalindrome(substring):
                potentialPals.append(substring)

    longestPal = potentialPals[0]
    for element in potentialPals:
        if len(element) > len(longestPal):
            longestPal = element

    return longestPal


while True:
    string = input("Enter a string only consisting of digits and letters: ")

    print(f"Longest palindromic substring: {longestPalindrome(string)}\n")