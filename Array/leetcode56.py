'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals = sorted(intervals,key = lambda start: start.start)
        l = intervals[0].start
        h = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start <= h:
                h = max(h,intervals[i].end)
            else:
                res.append([l,h])
                l = intervals[i].start
                h = intervals[i].end
        res.append([l,h])
        return res
