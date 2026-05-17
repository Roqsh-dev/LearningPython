

def getMaxSpacing(maxNum):
    return len( str(maxNum) ) + 2


def getLine(num, maxNum):
    line = ""

    for i in range(maxNum):

        number = str(num + (num * i))
        subtract = len( str(number) ) - 1

        line += " " * (getMaxSpacing(maxNum) - subtract) + number
    
    return line


while True:

    maxNumber= int( input("\n\nThe multiplication table should go from 1 to... ") )

    print("\n")

    for i in range(1, maxNumber + 1):
        print( getLine(i, maxNumber) )
