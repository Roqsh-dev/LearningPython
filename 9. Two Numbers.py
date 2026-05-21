

def getIndices(nums, target):
    prevNums = {
        # num: pos
    }
    indices = []

    for i in range(len(nums)):
        rest = target - int(nums[i])

        if rest == 0:
            indices.append(i)
            return indices
        
        elif rest in prevNums:
            indices.append( prevNums[rest] )
            indices.append(i)
            return indices
        
        prevNums[ int(nums[i]) ] = i
        

while True:
    givenNums = input("Please enter your list of numbers with spaces inbetween: ").split()
    targetNum = int( input("Please enter your target number: ") )

    indices = getIndices(givenNums, targetNum)
    print(f"Indices: {indices}\n")