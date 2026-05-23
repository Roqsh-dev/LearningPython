
def isTriangle(sidesList):

    sortedList = sorted(sidesList)

    if (sortedList[0] + sortedList[1]) <= sortedList[2]:
        print("This is no triangle!\n")
        return False
    else:
        return True


def hasRightAngle(sidesList):

    sortedList = sorted(sidesList)
    
    return sortedList[2] ** 2 == sortedList[1] ** 2 + sortedList[0] ** 2


while True:
    side1 = int(input("First side: "))
    side2 = int(input("Second side: "))
    side3 = int(input("Third side: "))

    Sides = [side1, side2, side3]

    triangle = isTriangle(Sides)

    if triangle:
        print(f"Has right Angle: {hasRightAngle(Sides)}\n")
