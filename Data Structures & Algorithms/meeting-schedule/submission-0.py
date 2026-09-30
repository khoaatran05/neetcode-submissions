"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0 or len(intervals) == 1:
            return True

        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):

            end = intervals[i-1].end
            begin = intervals[i].start

            if end > begin:
                return False

        return True
            






        
