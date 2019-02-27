import time
import random
import numpy as np

def MergeSort(nums):
    '''
    O(Nlog(N))
    nuns: [list]
    '''
    import pdb; pdb.set_trace()
    if len(nums) <= 1 : return nums
    l = int(len(nums)/2)       #二分分解
    left = MergeSort(nums[:l])
    right = MergeSort(nums[l:])

    return merge(left, right)


def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]    #到最后任何一个数组先出栈完，就将另外一个数组里的所有元素追加到新数组后面
    result += right[r:]
    return result




if __name__ =='__main__':
    nums = list(np.random.randint(100,size=100))
    print('The nums array before MergeSort : {}'.format(nums))
    start = time.time()
    nums_sorted = MergeSort(nums)
    end = time.time()
    print('The nums array after MergeSort : {}'.format(nums_sorted))
    print('MergeSort costs time : {} s'.format(end-start))
