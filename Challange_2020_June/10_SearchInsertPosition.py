# LeedCode June Challange Day 10
# Search Insert Position Problem

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

def tests():
	assert searchInsert([1,3,5,6], 5) == 2
	assert searchInsert([1,3,5,6], 2) == 1
	assert searchInsert([1,3,5,6], 7) == 4
	assert searchInsert([1,3,5,6], 0) == 0

	print("All Tests passed!")

def searchInsert(nums, target):
	# Brute-force solution
	# Check the target is smaller or equal to all elements - 
	# then insert it to the beginnig
	if(all(target <= k for k in nums)): return 0

	idx = 0

	while(idx != len(nums)-1):
		# loope through the array checking every number in between
		if(nums[idx]<= target <= nums[idx+1]):
			return idx+1
		idx += 1
	return idx + 1
