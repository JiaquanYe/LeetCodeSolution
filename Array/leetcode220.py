'''
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        a = set()  #储存搜索范围内的数
        l = len(nums)
        for idx,n in enumerate(nums):
            if t == 0:
                if n in a:
                    return True
            else:
                for a_item in a:
                    if abs(n-a_item)<=t:
                        return True
            a.add(n)
            if len(a)==k+1:
                a.remove(nums[idx-k])
        return False
