#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/4/6
# desc：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#       你可以假设数组中无重复元素。


class Solution(object):

    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)

        if target in nums:
            return nums.index(target)
        else:
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] > target:
                    high = mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    return mid

        return low


if __name__ == '__main__':
    s = Solution()
    r1 = s.searchInsert([1, 3, 5, 6], 4)
    print(r1)
    r2 = s.searchInsert([1, 3, 5, 6], 0)
    print(r2)
    r3 = s.searchInsert([1, 3, 5, 6], 8)
    print(r3)
    r4 = s.searchInsert([1, 3, 5, 6], 1)
    print(r4)
