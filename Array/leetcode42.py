'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #独考虑这个位置的容量是多少？
        #毫无疑问，我们只要知道，这个位置左边最高的那个边，和右边最高的那个边，两者取小的，然后再减去本身的大小，
        #那么结果就是这个位置的容量。
        #3遍历

        if height is None or len(height)==0:
            return 0

        n=len(height)
        res=0
        left_max, right_max = [0]*n,[0]*n

        left_max[0] = height[0]
        for idx in range(1,n):
            left_max[idx] = max(height[idx],left_max[idx-1])

        right_max[n-1] = height[n-1]
        for idx in range(n-2,-1,-1):
            right_max[idx] = max(height[idx],right_max[idx+1])

        for idx in range(1,n-1):  #第一个和最后不统计
            res += min(left_max[idx],right_max[idx]) - height[idx]

        return res
