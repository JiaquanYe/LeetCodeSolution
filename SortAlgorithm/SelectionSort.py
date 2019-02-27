import time
import random
import numpy as np

def SelectionSort(nums):
    '''
    O(n^2)
    nuns: [list]
    '''
    l = len(nums)
    for i in range(l):
        min_idx = i
        for j in range(i,l):     #search min value index O(n)
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[min_idx],nums[i] = nums[i],nums[min_idx]
    return nums

if __name__ =='__main__':
    nums = list(np.random.randint(100,size=100))
    print('The nums array before SelectionSort : {}'.format(nums))
    start = time.time()
    nums_sorted = SelectionSort(nums)
    end = time.time()
    print('The nums array after SelectionSort : {}'.format(nums_sorted))
    print('SelectionSort costs time : {} s'.format(end-start))
