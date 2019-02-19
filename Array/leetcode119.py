'''
杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
'''

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        pre = [1,1]
        for i in range(2,rowIndex+1):
            now = [1] *(i+1)
            for j in range(1,i):
                now[j] = pre[j-1] + pre[j]

            #result += [now]
            pre = now
        return now
