
'''

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

'''

def reverseNum(num):
    reversedNumList = []
    sNum = str(num)

    for digit in sNum:
        reversedNumList.append(digit)

    reversedNumList.reverse()

    reversedNumString = ""
    for i in range(len(reversedNumList)):
        reversedNumString += str(reversedNumList[i])

    return int(reversedNumString)

def convertToIntList(lst):
    intList = []
    for string in lst:
        intList.append(int(string))

    return intList

def addIntLists(lst1, lst2):
    lst1NumString = ""
    lst2NumString = ""

    for i in range(len(lst1)):
        lst1NumString += str(lst1[i])

    for i in range(len(lst2)):
        lst2NumString += str(lst2[i])

    return int(lst1NumString) + int(lst2NumString)


while True:
    list1 = convertToIntList( input("Enter your first list: ").split() )
    list2 = convertToIntList( input("Enter your second list: ").split() )

    list1.reverse()
    list2.reverse()

    solution = reverseNum(addIntLists(list1, list2))
    print(f"The solution is {solution}!\n")