
nums1 = [1, 1, 2]                      #2, nums = [1,2,_]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] #5, nums = [0,1,2,3,4,_,_,_,_,_]
nums3 = []

def removeDuplicates(nums: list[int]) -> int:
    if nums == []:
        return 0, []
    
    prev = nums[0]

    uniques = len(nums)

    numsCopy = sorted(nums)
    numsCopy.remove(prev)

    for n in numsCopy:
        if n == prev:
            nums.remove(n)
            #nums.append("_")
            uniques -= 1

        prev = n

    return uniques, nums


length, newNums = removeDuplicates(nums2)
print(f"{newNums} (Unique Nums: {length})")