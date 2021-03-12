#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：快速排序


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    # 选取基准值(可以随意选，暂时选取中间位置)
    mid = arr[len(arr) // 2]

    # 将基准值从原始数组中移除，否则重复
    arr.remove(mid)

    # 定义空数组，分别存放比基准值小/大的数值
    left_arr = []
    right_arr = []

    for x in arr:
        if x >= mid:
            right_arr.append(x)
        else:
            left_arr.append(x)

    return quick_sort(left_arr) + [mid] + quick_sort(right_arr)


if __name__ == '__main__':
    r1 = quick_sort([3, 6, 7, 4, 2, 0, 6])
    print(r1)

    r2 = quick_sort([3])
    print(r2)

    r3 = quick_sort([])
    print(r3)

    r4 = quick_sort([3, 6])
    print(r4)
