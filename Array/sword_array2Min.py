"""
把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组 [3，32，321] ，则打印出这三个数字能排成的最小数字为 321323 。
"""

def getMax(str1,str2):
    """
        compare str1+str2 and str2+str1, return max
    """
    return str2 if str1+str2 < str2+str1 else str1

def array2Min(array):
    str_array = []
    for a in array:
        str_array.append(str(a))

    # bubble sort
    for idx in range(len(str_array)-1):
        for j in range(len(str_array)-idx-1):
            maxStr = getMax(str_array[j], str_array[j+1])
            #the max str in before,swap
            if maxStr == str_array[j]:
                str_array[j], str_array[j+1] = str_array[j+1], str_array[j]

    return str_array

if __name__ == "__main__":
    array = [3, 32, 321]
    result = array2Min(array)
