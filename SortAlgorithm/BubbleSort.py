import time
import random
import numpy as np

def BubbleSort(nums):
    '''
    O(n^2)
    nuns: [list]
    '''
    l = len(nums)
    for select_idx in range(l):
        for idx in range(select_idx+1,l):
            if nums[select_idx] > nums[idx]:
                nums[select_idx], nums[idx] = nums[idx], nums[select_idx]
    return nums

def Bubble_Sort(array):
    for i in range(len(array)-1):
        flag = False
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:              #没有交换元素了，可以break
           break
    return array

if __name__ =='__main__':
    nums = list(np.random.randint(1000,size=1000))
    print('The nums array before BubbleSort : {}'.format(nums))
    start1 = time.time()
    nums_sorted1 = Bubble_Sort(nums)
    end1 = time.time()
    start2 = time.time()
    nums_sorted2 = BubbleSort(nums)
    end2 = time.time()
    print('The nums array after Bubble_Sort : {}'.format(nums_sorted1))
    print('The nums array after BubbleSort : {}'.format(nums_sorted2))
    print('Bubble_Sort costs time : {} s'.format(end1-start1))
    print('BubbleSort costs time : {} s'.format(end2-start2))
