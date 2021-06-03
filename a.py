#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/4/14
# desc：
# 
# 影响因素：
#   1.
#   2.
# 检查点：
#   1.
# 测试用例：
#   0.


class Solution(object):
    def minArray(self, s):
        """
        :type numbers: List[int]
        :rtype: int
        """

        #numbers.sort()

        dic = {}

        for i in s:
            if dic.get(i) is None:
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1

        for k, v in dic.items():
            if v == 1:
                return k

        return ' '

s = Solution()
r = s.minArray('leetcode')
print(r)
