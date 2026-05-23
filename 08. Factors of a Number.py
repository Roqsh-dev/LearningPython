

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

def format(factors):
    string = ""
    length = len(factors)

    for i in range(length):
        if i == length - 1:
            string += f"{factors[i]}"
        else:
            string += f"{factors[i]}, "

    return string


while True:
    number = int( input("Enter a number to get all possible factors: ") )
    factors = getFactors(number)

    print(format(factors))
    
    if isPrime(factors, number):
        print("Note: Your entered number IS a prime!\n")
    else:
        print("Note: Your entered number is NO prime.\n")