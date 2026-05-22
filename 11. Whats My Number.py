
'''

Between 1 and 1000, there is only 1 number that meets the following criteria:

- The number has two or more digits.
- The number is prime.
- The number does NOT contain a 1 or 7 in it.
- The first two digits add up to be odd.
- The second to last digit is even and greater than 1.
- The last digit is equal to how many digits are in the number.
- The sum of all of the digits is less than or equal to 10.

'''

def getFactors(num):
    if num == 0:
        return [0]
    
    Factors = [1]

    for i in range(2, num + 1):
        if num % i == 0:
            Factors.append(i)

    return sorted(Factors)

def isPrime(factors, num):
    if num == 0 or num == 1:
        return False
    elif factors[0] == 1 and factors[1] == num:
        return True
    
    return False


for i in range(10, 1001):

    numInDigits = []

    if not isPrime(getFactors(i), i):
        continue

    iString = str(i)
    iLength = len(iString)
    for digit in iString:
        numInDigits.append(digit)

    if "1" in numInDigits or "7" in numInDigits:
        continue

    if ( (int(numInDigits[0]) + int(numInDigits[1])) % 2 ) == 0:
        continue

    if not iLength == int(numInDigits[iLength - 1]):
        continue

    sum = 0
    for digit in numInDigits:
        sum += int(digit)
    if not sum <= 10:
        continue

    if int(numInDigits[iLength - 2]) > 1 and int(numInDigits[iLength - 2]) % 2 == 0:
        print(f"The number is {i} !")
        break