'''
将一个字符串(数字)转换成一个整数，要求不能使用字符串转换整数的库函数
'''

def str2int(s):
    flag = False
    if s in None:
        return None`
    if len(s)<1:
        return None
     dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    nums_stack = []
    for i in s:
        if i in dict.keys():
            numStack.append(dict[i])
        elif i == '+':
            continue
        elif i == '-':
            continue
        else:
            return 0

    print(numStack)
    ans = 0
    if len(numStack) == 1 and numStack[0] == 0:
        flag = True
        return 0
    for i in numStack:
        ans = ans*10 + i
    if s[0] == '-':
        ans = 0 - ans
    return ans
