# LeedCode June Challange Day 11
# Sort Colors Problem

# Given an array with n objects colored red, white or blue, 
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, 
# white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def test():
    assert sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
    assert sortColors([2,0,1]) == [0,1,2]
    assert sortColors([0,1,2]) == [0,1,2]
    assert sortColors([0,0,1,1,2,2]) == [0,0,1,1,2,2]
    assert sortColors([2,0,2,1,0,1,1,0]) == [0,0,0,1,1,1,2,2]

    print("All tests passed!")

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    cur = 0
    left = 0
    right = len(nums) - 1

    for _ in range(len(nums)):
        if(nums[cur] == 0):
            nums[left], nums[cur] = nums[cur], nums[left]
            cur  += 1
            left += 1
        elif(nums[cur] == 2):
            nums[right], nums[cur] = nums[cur], nums[right]
            right -= 1
        else:
            cur += 1

    return nums

test()