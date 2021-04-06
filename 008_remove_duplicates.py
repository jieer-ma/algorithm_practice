#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/30
# desc：给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
#       不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


class Solution(object):
    def removeDuplicates(self, nums):
        nums2 = nums[:]

        for i in nums2:
            if nums.count(i) == 1:
                continue
            else:
                nums.remove(i)

        return nums


if __name__ == '__main__':
    s = Solution()
    r1 = s.removeDuplicates([0, 0, 1, 1, 2, 3])
    print(r1)
    r2 = s.removeDuplicates([1, 1, 2])
    print(r2)