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

def insertSort(array):
    if len(array)<=1:
        return array
    for i in range(1,len(array)):
        value = array[i]
        for j in range(i)[::-1]:  #查找位置，并后移元素
            if value < array[j]:
                array[j+1] = array[j]
            else:
            	break
        array[j+1] = value          #在j后插入
    return array



if __name__ =='__main__':
    nums = list(np.random.randint(10000,size=10000))
    print('The nums array before InsertionSort : {}'.format(nums))
    start = time.time()
    nums_sorted = InsertionSort(nums)
    end = time.time()
    print('The nums array after InsertionSort : {}'.format(nums_sorted))
    print('InsertionSort costs time : {} s'.format(end-start))
