#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组


def merge_arr(arr1, arr2):
    # 数组 arr1和arr2 最大下标
    i = len(arr1) - 1
    j = len(arr2) - 1

    # 合并后 arr1 最大下标
    total = len(arr1) + len(arr2) - 1

    # todo 暂时用补0方式扩充arr1长度
    for x in range(0, len(arr2)):
        arr1.append(0)

    # 将arr1和arr2元素按照由大到小填充到 arr1 数组中(从数组大的小标开始填充)
    while i >= 0 and j >= 0:
        if arr1[i] >= arr2[j]:
            arr1[total] = arr1[i]
            i = i - 1
            total = total - 1
        else:
            arr1[total] = arr2[j]
            j = j - 1
            total = total - 1

    while j >= 0:
        arr1[total] = arr2[j]
        j = j - 1
        total = total - 1

    print(arr1)


if __name__ == '__main__':
    merge_arr([1, 2], [2, 3, 4])
    merge_arr([3, 4], [1, 2, 3])
    merge_arr([1, 2, 3], [4, 5])
    merge_arr([3, 4, 5], [1, 2])
    merge_arr([1, 3], [1, 2])
    merge_arr([1, 2], [1, 3])
    merge_arr([1, 2], [])
    merge_arr([], [1, 2])