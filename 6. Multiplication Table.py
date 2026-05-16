

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

    # we need to add +1 to maxNumber because we skip i=0
    for i in range(maxNumber + 1):
        if not i == 0:
            print( getLine(i, maxNumber) )
