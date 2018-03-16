'''
243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
 Assume that words = ["practice", "makes", "perfect", "coding", "makes"]. 

Given word1 = “coding”, word2 = “practice”, return 3.
 Given word1 = "makes", word2 = "coding", return 1. 

Note:
 You may assume that word1 does not equal to word2, and word1 and word2 are both in the list. 

'''
# Naive approach
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        start = 0
        end = 0
        shortestDist = len(words) +1
        
        for i in range(len(words)):
            if words[i] == word1:
                start = i
                
                for j in range(i, len(words)):
                    if words[j] == word2:
                        end = j
                        print start, end
                        if end - start < shortestDist:
                            shortestDist = j - i
            if words[i] == word2:
                start = i
                
                for j in range(i, len(words)):
                    if words[j] == word1:
                        end = j
                        if end - start < shortestDist:
                            shortestDist = j - i
        return shortestDist


# Better approach
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
       
        shortestDist = len(words) +1
        word1Index = []
        word2Index = []
        # create a list for both words to store the indexes 
        for i in range(len(words)):
            if words[i] == word1:
                word1Index.append(i)
            elif words[i] == word2:
                word2Index.append(i)
        
        # now loop the index lists to find shortest distance
        for i in range(len(word1Index)):
            for j in range(len(word2Index)):
                if abs(word1Index[i] - word2Index[j]) < shortestDist:
                    shortestDist = abs(word1Index[i] - word2Index[j])
        
           
        return shortestDist		

# Another approach would be to store the most recent indexes		
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
       
        shortestDist = len(words) +1
        word1Index = -1
        word2Index = -1
        # store the last found index
        for i in range(len(words)):
            if words[i] == word1:
                word1Index = i
            elif words[i] == word2:
                word2Index = i
        
            # check if it is the shortest distance
            if word1Index != -1 and word2Index != -1:
                shortestDist = min(shortestDist,abs(word1Index - word2Index))
        
           
        return shortestDist