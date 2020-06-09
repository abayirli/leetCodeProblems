# LeedCode June Challange Day 8
# Power of Two Problem

# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 20 = 1


def isPowerOfTwo(n: int) -> bool:
	#convert to binary and make the digits a list
    binary = list("{0:b}".format(n))

    #check for 0 and 1
    if(len(binary) == 1):
        check = (binary[0] == '1')
    
    #check for other 2's powers
    #true if the first digit is 1 and the remaining digits are all zeros
    else:
        check = (binary[0] == '1' and set(binary[1:]) == set(['0']))

    return check


def main():
    print(f"is 15 a power of 15: {isPowerOfTwo(15)}")

if __name__ == "__main__":
    main()
