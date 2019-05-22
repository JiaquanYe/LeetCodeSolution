"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

solution:
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
"""

def searchArray(array,target):
    row = 0
    col = len(array[0])-1
    cur = None
    while -1<row<len(array) and -1<col<len(array):
        cur = array[row][col]
        if cur < target:
            row += 1
        elif cur > target:
            col -= 1
        elif target == cur:
            return True
    return False

if __name__ == "__main__":
    array = [[1,2,3],[4,5,6],[7,8,9]]
    flag = searchArray(array, 12)
