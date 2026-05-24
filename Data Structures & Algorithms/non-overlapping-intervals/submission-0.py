class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                # no overlap, keep this interval
                prev_end = end
            else:
                # overlap, remove one interval
                removals += 1
                # keep the interval with smaller end
                prev_end = min(prev_end, end)

        return removals