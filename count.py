# 递归版
def count(lst, target):
    if len(lst) == 0:
        return 0
    if lst[0] == target:
        return 1 + count(lst[1:], target)
    else:
        return count(lst[1:], target)


# 迭代版
def for_count(lst, target):
    counter = 0
    # 对 lst 中的每一个 element, 都执行这个操作
    for item in lst:
        if item == target:
            counter = counter + 1
    return counter


# 尾递归版
def inner(counter, lst, target):
    if len(lst) == 0:
        return counter
    if lst[0] == target:
        return inner(counter+1, lst[1:], target)
    return inner(counter, lst[1:], target)


def tail_count(lst, target):
    return inner(0, lst, target)


# while 循环 版
def while_count(lst, target):
    counter = 0
    while True:
        if len(lst) == 0:
            break
        if lst[0] == target:
            counter += 1
            lst = lst[1:]
        else:
            lst = lst[1:]
    return counter


'''
如果 数组中没有数字 返回0
如果 数组中第一个数字大于0 返回 1 + 剩余大于100的个数
否则 返回剩余大于100 的个数
'''

if __name__ == '__main__':
    array = [1, 101, 2, 2, 202]
    print(count(array, 2))
    print(tail_count(array, 2))
    print(for_count(array, 2))
    print(while_count(array, 2))

