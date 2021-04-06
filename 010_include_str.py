#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/31
# desc：实现 strStr() 函数。
#       给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


class Solution(object):
    def strStr(self, haystack, needle):
        i = 0

        while i <= (len(haystack) - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i

            i = i + 1

        return -1


if __name__ == '__main__':
    s = Solution()
    # 预期： 2
    r1 = s.strStr('hello', 'll')
    print(r1)
    # 预期： 0
    r2 = s.strStr('hello', 'he')
    print(r2)
    # 预期： -1
    r3 = s.strStr('hello', 'eb')
    print(r3)
    # 预期： -1
    r4 = s.strStr('hello', 'abc')
    print(r4)
    # 预期： 0
    r5 = s.strStr('hello', 'hello')
    print(r5)
    # 预期： -1
    r6 = s.strStr('hello', 'hello1')
    print(r6)
    # 预期： 0
    r7 = s.strStr('hello', '')
    print(r7)


