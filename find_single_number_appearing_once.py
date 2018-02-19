'''
136. Single Number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

# my solution - use Hash table to store the counts of every element in the array
# and then check the hash table where it is equal to 1
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashNum = {}
        for i in range(len(nums)):
            if nums[i] in hashNum:
                hashNum[nums[i]] += 1
            else:
                hashNum[nums[i]] = 1
        for i in range(len(nums)):
            if hashNum[nums[i]] == 1:
                return nums[i]

'''
Approach #2 Hash Table [Accepted]

Algorithm

We use hash table to avoid the O(n)O(n) time required for searching the elements.

Iterate through all elements in \text{nums}nums
Try if hash\_tablehash_table has the key for pop
If not, set up key/value pair
In the end, there is only one element in hash\_tablehash_table, so use popitem to get it
Python
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
'''
Complexity Analysis

Time complexity : O(n * 1) = O(n)O(n∗1)=O(n). Time complexity of for loop is O(n)O(n). Time complexity of hash table(dictionary in python) operation pop is O(1)O(1).

Space complexity : O(n)O(n). The space required by hash\_tablehash_table is equal to the number of elements in \text{nums}nums.
'''


'''
Approach #3 Math [Accepted]

Concept

2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c

Python
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


'''
Complexity Analysis

Time complexity : O(n + n) = O(n)O(n+n)=O(n). sum will call next to iterate through \text{nums}nums. We can see it as sum(list(i, for i in nums)) which means the time complexity is O(n)O(n) because of the number of elements(nn) in \text{nums}nums.

Space complexity : O(n + n) = O(n)O(n+n)=O(n). set needs space for the elements in nums
'''


'''
Approach #4 Bit Manipulation [Accepted]

Concept

If we take XOR of zero and some bit, it will return that bit
a \oplus 0 = aa⊕0=a
If we take XOR of two same bits, it will return 0
a \oplus a = 0a⊕a=0
a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
So we can XOR all bits together to find the unique number.

Python
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
'''
Complexity Analysis

Time complexity : O(n)O(n). We only iterate through \text{nums}nums, so the time complexity is the number of elements in \text{nums}nums.

Space complexity : O(1)O(1).
'''

