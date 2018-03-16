'''
520. Detect Capital 
Given a word, you need to judge whether the usage of capitals in it is right or not. 

We define the usage of capitals in a word to be right when one of the following cases holds: 
1.All letters in this word are capitals, like "USA".
2.All letters in this word are not capitals, like "leetcode".
3.Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way. 

Example 1:

Input: "USA"
Output: True



Example 2:

Input: "FlaG"
Output: False



Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters. 
'''

# Based on ASCII value of small and capital letters
# Capital letters have range of 65-90 and small letter have range of 97-122
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        arr = list(word)
        flip = 0
        
        if len(arr) == 1 or len(arr) == 0:
            return True
        
        if ord(arr[0]) <= 90 and ord(arr[0]) >=65 and ord(arr[1]) <= 90 and ord(arr[1]) >=65:
            for i in range(2,len(arr)):
                if ord(arr[i]) > 90:
                    return False
                
        if ord(arr[0]) <= 90 and ord(arr[0]) >=65 and ord(arr[1]) > 90:
            for i in range(2,len(arr)):
                if ord(arr[i]) <= 90:
                    return False
                
        if ord(arr[0]) > 90:
            print "this case"
            for i in range(1,len(arr)):
                print ord(arr[i])
                if ord(arr[i]) <= 90:
                    return False
        
        return True