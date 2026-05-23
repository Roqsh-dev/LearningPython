

print("\nThe Fibonacci Sequence starts with [0, 1, ...]")

def getFibonacciNum(pos):

    Sequence = [0, 1]

    for i in range(2, pos + 1):
        Sequence.append( Sequence[i - 2] + Sequence[i - 1] )

    return Sequence[pos]

while True:

    requestedPos = int( input("Enter the position you want to get the number from: ") )

    #we do -1 to match the requestedPos with the pos in our sequence
    fibonacciNum = str(getFibonacciNum(requestedPos - 1))

    print(f"The number is {fibonacciNum}\n")
