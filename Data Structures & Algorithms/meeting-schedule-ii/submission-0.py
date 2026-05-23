"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        s = 0
        e = 0
        rooms = 0
        ans = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                ans = max(ans, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1

        return ans