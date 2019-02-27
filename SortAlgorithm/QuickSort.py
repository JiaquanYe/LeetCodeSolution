import time
import numpy as np
import pandas as pd

def QuickSort(nums,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        left_pointer, right_pointer  = start,end
        #设置基准数
        base = nums[start]
        while left_pointer < right_pointer:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while nums[right_pointer] >= base and left_pointer < right_pointer:
                right_pointer -= 1
            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            nums[left_pointer] = nums[right_pointer]

            #同样的方式比较前半区
            while nums[left_pointer] <= base and left_pointer < right_pointer:
                left_pointer += 1
            nums[right_pointer] = nums[left_pointer]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        nums[left_pointer] = base
         #递归前后半区
        QuickSort(nums,start,left_pointer-1)
        QuickSort(nums,right_pointer+1,end)
    return nums

if __name__ =='__main__':
    nums = list(np.random.randint(100,size=100))
    print('The nums array before QuickSort : {}'.format(nums))
    start = time.time()
    nums_sorted = QuickSort(nums,0,len(nums)-1)
    end = time.time()
    print('The nums array after QuickSort : {}'.format(nums_sorted))
    print('QuickSort costs time : {} s'.format(end-start))
