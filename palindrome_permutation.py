'''
266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a string is Palindrome of the each charater appears for even number of times
        # and only character can appear for odd number of times
        # so we count the characters using Hash map and then count
        myLetters = {}
        for i in range(len(s)):
            if s[i] in myLetters:
                #print s[i]
                myLetters[s[i]] += 1
            else:
                myLetters[s[i]] = 1
        #print myLetters
        countOdd = 0
        for k in myLetters:
            #print myLetters[k]
            if myLetters[k]%2 <> 0:
                countOdd = countOdd + 1
                #print "countOdd", countOdd
                if countOdd > 1:
                    return False
        return True