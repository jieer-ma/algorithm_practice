#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：递归实现数组中成员是否按从小到大排序的判断，是则返回0，否则返回1


def arr_sort(arr, arr_len):

    if(arr_len == 0):
        return 1
    if(arr_len == 1):
        return 1

    return (arr[arr_len-1] >= arr[arr_len-2]) and (arr_sort(arr, arr_len-1))


if __name__ == '__main__':
    r1 = arr_sort([1, 2, 3, 4, 0, 4, 2], 7)
    print(r1)

    r2 = arr_sort([1, 2, 3, 4], 4)
    print(r2)

    r3 = arr_sort([], 0)
    print(r3)

    r4 = arr_sort([1], 1)
    print(r4)