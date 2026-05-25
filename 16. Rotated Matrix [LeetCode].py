
#mat = [ [5,1,9,11], [2,4,8,10], [13,3,6,7], [15,14,12,16] ]
#out = [ [15,13,2,5], [14,3,4,1], [12,6,8,9], [16,7,10,11] ]

#mat2 = [[1,2,3],[4,5,6],[7,8,9]]
#out2 = [[7,4,1],[8,5,2],[9,6,3]]


def rotate90Degrees(matrix):
    rotatedMatrix = []

    rowLength = len(matrix[0])
    matLength = len(matrix)

    # number
    for n in range(rowLength):

        rotatedRow = []
        # row
        for r in range(matLength-1, -1, -1):
            row = matrix[r]
            num = row[n]
            rotatedRow.append(num)
        
        rotatedMatrix.append(rotatedRow)

    return rotatedMatrix
    #for LeetCode: matrix[:] = rotatedMatrix

#print(rotate90Degrees(mat2))