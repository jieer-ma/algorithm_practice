#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/17
# desc：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#       你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#       你可以按任意顺序返回答案。


def two_nums_sum(arr, target):
    arr_len = len(arr)
    target_arr = []

    for i in range(0, arr_len -1):
        for j in range(i + 1, arr_len):
            if arr[i] + arr[j] == target:
                # 如果之前有匹配的数据，先清空，保证按组输出
                target_arr.clear()
                target_arr.append(i)
                target_arr.append(j)
                print(target_arr)
            else:
                continue


if __name__ == '__main__':
    two_nums_sum([2, 8, 9, 3], 11)
    two_nums_sum([2, 8, 0, 1], 11)
    two_nums_sum([2, 8, 9, 3, 8], 11)

