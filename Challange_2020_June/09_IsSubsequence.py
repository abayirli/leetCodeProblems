# LeedCode June Challange Day 9
# Is Subsequence Problem

# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative
# positions of the remaining characters. 
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


def test():
	assert isSubsequence(s = "axc", t = "ahbgdc") == False
	assert isSubsequence(s = "abc", t = "ahbgdc") == True
	assert isSubsequence(s = "abbc", t = "ahbgdbc") == True
	assert isSubsequence(s = "abc", t = "abc") == True
	assert isSubsequence(s = "aaaaaa", t="bbaaaa") == False
	print("All tests passed!")

def isSubsequence(s: str, t: str) -> bool:
	
	if s == "": return True

	i = 0; j = 0
	while(j < len(t) and i != len(s)):
		if(s[i] == t[j]):
			i += 1
		j += 1
	return (i == len(s))

def main():
	test()

if __name__ == "__main__":
	main()
