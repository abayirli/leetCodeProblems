# LeedCode June Challange Day 4
# Reverse a String Problem
# Write a function that reverses a string. The input string is given as an array of characters char[].
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()