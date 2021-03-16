#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/15
# desc：一个数组找出重复的元素


def repeat_element(arr):
    arr_dict = {}
    repeat_count = 0
    repeat_elements = []

    for x in arr:
        if arr_dict.get(x) is None:
            arr_dict[x] = 1
        else:
            arr_dict[x] = arr_dict[x] + 1

    for k, v in arr_dict.items():
        if v > 1:
            repeat_count = repeat_count + 1
            repeat_elements.append(k)

    if len(repeat_elements) > 0:
        print(arr, '一共有 ', repeat_count, ' 个重复元素，分别是：', repeat_elements)
    else:
        print('没有重复元素')


if __name__ == '__main__':
    # 有一个重复元素
    repeat_element([1, 2, 5, 6, 8, 1])
    # 有两个重复元素
    repeat_element([1, 2, 5, 6, 8, 1, 5])
    # 全部都是重复元素
    repeat_element([3, 3, 3, 3])
    # 没有重复元素
    repeat_element([1, 2, 5, 6, 8])