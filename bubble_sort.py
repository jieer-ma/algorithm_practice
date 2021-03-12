#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：冒泡排序


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

    return arr


if __name__ == '__main__':
    r1 = bubble_sort([0, 5, 3, 2, 9, 20, 6, 7, 3])
    print(r1)
