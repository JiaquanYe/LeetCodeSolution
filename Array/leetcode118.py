'''
杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
'''


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(numRows):
            temp=[1]*(i+1)
            res.append(temp)
            for j in range(1,i):#列
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
