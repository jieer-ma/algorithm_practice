#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/30
# desc：编写一个函数来查找字符串数组中的最长公共前缀。
#       如果不存在公共前缀，返回空字符串 ""。


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        s1 = min(strs)
        s2 = max(strs)

        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[0:i]

        return s1


if __name__ == '__main__':
    s = Solution()
    r1 = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(r1)
    r2 = s.longestCommonPrefix(["dog","racecar","car"])
    print(r2)
    r3 = s.longestCommonPrefix(["abc", "abcdf", "abcddfg"])
    print(r3)
    r4 = s.longestCommonPrefix(["", "b"])
    print(r4)