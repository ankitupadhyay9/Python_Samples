'''
Implement strStr(). 

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLen = len(needle)
        i = 0
        while i < len(haystack)-needleLen+1:
            if haystack[i:i+needleLen] == needle:
                return i
            i = i + 1
        return -1