
#  #  #    #  #  #     #  #  #
#  0  #    #  1  #     #  2  #
#  #  #    #  #  #     #  #  #

#  #  #    #  #  #     #  #  #
#  3  #    #  4  #     #  5  #
#  #  #    #  #  #     #  #  #

#  #  #    #  #  #     #  #  #
#  6  #    #  7  #     #  8  #
#  #  #    #  #  #     #  #  #


def isValidSudoku(board: list[list[str]]) -> bool:

    # check rows
    for row in board:
        numsR = []

        for n in row:
            if n == ".":
                continue

            if not n in numsR:
                numsR.append(n)
            else:
                return False
            
    # check columns
    for i in range(9):
        numsC = []

        for row in board:
            if row[i] == ".":
                continue

            if not row[i] in numsC:
                numsC.append(row[i])
            else:
                return False
            
    # check boxes
    for b in range(9):
        numsB = []
        boxRows = []

        # 3x3 box - 3 rows of length 3
        for j in range(3):

            if b == 0 or b == 1 or b == 2:
                r = j
                p = b
            elif b == 3 or b == 4 or b == 5:
                r = j + 3
                p = b - 3
            else:
                r = j + 6
                p = b - 6     
            
            boxRows.append(board[r][(p*3):3+(p*3)])

        #print(boxRows)

        for row in boxRows:
            for i in range(3):
                if row[i] == ".":
                    continue

                if not row[i] in numsB:
                    numsB.append(row[i])
                else:
                    return False


    return True



board1 = [ #true
    ["5","3",".",  ".","7",".",  ".",".","."],
    ["6",".",".",  "1","9","5",  ".",".","."],
    [".","9","8",  ".",".",".",  ".","6","."],

    ["8",".",".",  ".","6",".",  ".",".","3"],
    ["4",".",".",  "8",".","3",  ".",".","1"],
    ["7",".",".",  ".","2",".",  ".",".","6"],

    [".","6",".",  ".",".",".",  "2","8","."],
    [".",".",".",  "4","1","9",  ".",".","5"],
    [".",".",".",  ".","8",".",  ".","7","9"]
]

board2 = [ #false
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board1))