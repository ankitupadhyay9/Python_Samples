'''
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
'''

# Solution is to sort the array first using start time
# since intervals are not sorted and then compare end time of one meeting with end time 
# of another meeting

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    
    
    def sortInterval(self,intervals2):
        def merge(a,b):
            c = []
            while len(a) > 0 and len(b) > 0:
                if a[0].start > b[0].start:
                    c.append(b[0])
                    b.remove(b[0])
                else:
                    c.append(a[0])
                    a.remove(a[0])
            if len(a) == 0:
                c = c + b
            else:
                c = c + a
            return c
    
        if len(intervals2) == 1 or len(intervals2) == 0:
            return intervals2
        #print len(intervals2)
        mid = int(len(intervals2)/2)
        #print "mid:", mid
        a = self.sortInterval(intervals2[:mid])
        b = self.sortInterval(intervals2[mid:])
        return merge(a,b)
        
        
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # sort the input using MergeSort Algo
        intervals = self.sortInterval(intervals)
        for i in range(1,len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
                
        