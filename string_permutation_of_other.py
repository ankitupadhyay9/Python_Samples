# this function checks if a string is permutation of other string


def checkPermutation(str1, str2):
	if len(str1) != len(str2):
		return False
	else:
		str1Sorted = sorted(str1.lower())
		str2Sorted = sorted(str2.lower())

		s=""

		if s.join(str1Sorted) == s.join(str2Sorted):
			return True
		else:
			return False

print str(checkPermutation("abc","DEF"))