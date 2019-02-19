'''
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4
'''
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #可以把这个问题考虑为数字在数轴上的覆盖，我们使用一个哈希表存储连续数值的端点和对应的长度，
        #这样如果新遍历的数左边或右边可以和已有的区间连上的话就可以对原有的区间进行扩张。
        n = len(nums)
        d = {}
        ans = 0
        for i in nums:
            if i not in d:
                left = d.get(i-1, 0)
                right = d.get(i+1, 0)
                length = left + right + 1
                ans = max(ans, length)

                d[i] = length
                d[i-left] = length
                d[i+right] = length

        return ans
