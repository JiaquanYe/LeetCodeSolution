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

if __name__ =='__main__':
    nums = list(np.random.randint(1000,size=1000))
    print('The nums array before BubbleSort : {}'.format(nums))
    start = time.time()
    nums_sorted = BubbleSort(nums)
    end = time.time()
    print('The nums array after BubbleSort : {}'.format(nums_sorted))
    print('BubbleSort costs time : {} s'.format(end-start))
