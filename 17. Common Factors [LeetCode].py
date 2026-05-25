

def getCommonFactors(a, b):
        factorsA = getFactors(a)
        factorsB = getFactors(b)

        commonFacts = []

        for factor in factorsA:
            if factor in factorsB:
                commonFacts.append(factor)

        return len(commonFacts)


def getFactors(num):
    if num == 0:
        return [0]
    
    Factors = [1]

    for i in range(2, num + 1):
        if num % i == 0:
            Factors.append(i)

    return sorted(Factors)