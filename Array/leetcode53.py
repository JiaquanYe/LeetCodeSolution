'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        l = len(nums)
        for idx in range(1,l):
            ##当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            nums[idx] = max(nums[idx]+nums[idx-1],nums[idx])
        return max(nums)
