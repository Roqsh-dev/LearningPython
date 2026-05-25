

# "Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."

def reverseNum(x):
    reversedNumList = []
    sNum = str(x)

    for digit in sNum:
        if not digit == "-":
            reversedNumList.append(digit)

    reversedNumList.reverse()

    reversedNumString = ""
    for i in range(len(reversedNumList)):
        reversedNumString += str(reversedNumList[i])

    if "-" in sNum:
        reversedNumString = "-" + reversedNumString

    reversedNum = int(reversedNumString)
    if reversedNum > (2**31 - 1) or reversedNum < (-2**31):
        return 0
    else:
        return reversedNum