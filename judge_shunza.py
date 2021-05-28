#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/12
# desc：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2-10为数字本身，
#       A为1，J为11，Q为12，K为13，而大小王可以看成任意数字，也就是说王可以充当任何一张牌来组成顺子。


def is_shunza(arr):
    # 数组正序排序
    arr.sort()
    # 牌里面大小王(即0)的个数
    count_0 = 0

    for i in range(0, 4):
        if arr[i] == 0:
            count_0 = count_0 + 1
        elif arr[i] == arr[i+1]:
            return False

    return arr[4] - arr[count_0] < 5


if __name__ == '__main__':
    # 顺子
    r1 = is_shunza([3, 6, 4, 5, 7])
    print(r1)

    # 非顺子
    r2 = is_shunza([3, 6, 4, 5, 8])
    print(r2)

    # 顺子
    r3 = is_shunza([4, 7, 6, 5, 0])
    print(r3)

    # 顺子
    r4 = is_shunza([4, 0, 6, 5, 0])
    print(r4)

    # 顺子
    r4 = is_shunza([1, 0, 3, 5, 0])
    print(r4)




