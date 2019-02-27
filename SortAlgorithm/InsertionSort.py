import time
import random
import numpy as np

def InsertionSort(nums):
    '''
    O(n^2)
    nuns: [list]
    '''
    l = len(nums)
    for i in range(1,l):
        selected = nums[i]
        if selected < nums[i-1]:
            for j in range(i-1,-1,-1):
                if selected < nums[j]:
                    nums[j+1] = nums[j]
                    index = j         #记录待插入下标
                else:
                    break
            nums[index] = selected
    return nums



if __name__ =='__main__':
    nums = list(np.random.randint(10000,size=10000))
    print('The nums array before InsertionSort : {}'.format(nums))
    start = time.time()
    nums_sorted = InsertionSort(nums)
    end = time.time()
    print('The nums array after InsertionSort : {}'.format(nums_sorted))
    print('InsertionSort costs time : {} s'.format(end-start))
