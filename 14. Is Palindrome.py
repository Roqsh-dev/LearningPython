

def isPalindrome(num):
    string = str(num)
    digitList = []

    for digit in string:
        digitList.append(digit)

    reversedString = ""
    for i in range(len(digitList) - 1, -1, -1):
        reversedString += digitList[i]

    return string == reversedString


while True:
    num = input("Enter your number: ")

    while not num.isdigit():
        num = input("Please enter a number: ")

    if isPalindrome(num):
        print("Your number IS a palindrome!\n")
    else:
        print("Your number isnt a palindrome.\n")