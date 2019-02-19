'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #greedy algorithm, two pointer.
        #盛水容量由矮的高度决定，所以我们每次移动矮的高度.

        left = 0
        right = len(height)-1
        res = 0

        while left<right:
            cur_res = (right-left)*height[right] if height[left] > height[right] else  (right-left)*height[left]
            res = max(res,cur_res)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return res
