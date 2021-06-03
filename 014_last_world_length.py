#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/4/8
# desc：给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。
#       单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。


class Solution(object):
    def lengthOfLastWorld(self, s):
        s = s[::-1].lstrip()

        if not s:
            return 0
        else:
            for i in range(0, len(s)):
                if s[i] == ' ':
                    return i
                elif i == len(s) - 1:
                    return len(s)


if __name__ == '__main__':
    s = Solution()
    r1 = s.lengthOfLastWorld('Hello World! ')
    print(r1)
    r2 = s.lengthOfLastWorld('')
    print(r2)
    r3 = s.lengthOfLastWorld('a')
    print(r3)