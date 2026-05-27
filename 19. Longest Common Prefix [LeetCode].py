

def shortestStringLength(strs):
    stringLengths = []
    for s in strs:
        stringLengths.append(len(s))
    
    stringLengths = sorted(stringLengths)
    return stringLengths[0]


def longestCommonPrefix(strs: list[str]):
    if not strs:
        return ""
    
    strsAsDigitList = []
    for s in strs:
        list = []
        for d in s:
            list.append(d)
        strsAsDigitList.append(list)

    commonPrefix = ""
    # digit
    for d in range(shortestStringLength(strs)):
        currentDigit = strsAsDigitList[0][d]
        allSame = True

        for digitList in strsAsDigitList:
            if digitList[d] != currentDigit:
                allSame = False
                break

        if allSame:
            commonPrefix += currentDigit
        else:
            break

    return commonPrefix

             
#strs = ["flower", "flow", "flight"]

#print(longestCommonPrefix(strs))