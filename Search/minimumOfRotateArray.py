"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

二分查找的变形，注意到旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。
与二分查找不同，二分查找需要对比区间的首尾元素，然后根据比对缩小区间;
此题只需要取区间的中间元素与首尾对比，然后根据对比缩小区间

reference : https://www.cnblogs.com/klchang/p/7783386.html
"""

def findMinOfRotateArray(rotate_array):
    n = len(rotate_array)
    mid = (n-1)/2
    while mid > -1 and mid < n:
        # 如果中间点小于尾元素，说明最小数字在前一半
        if rotate_array[mid] < rotate_array[-1]:
            rotate_array = rotate_array[:mid+1]
            findMinOfRotateArray(rotate_array)
        # 如果中间点大于首元素，说明最小数字在后面一半
        elif rotate_array[mid] > rotate_array[1]:
            rotate_array = rotate_array[mid+1:]
            findMinOfRotateArray(rotate_array)
