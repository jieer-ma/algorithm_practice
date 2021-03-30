#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/30
# desc：给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#       回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if x == y:
                return True
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    r1 = s.isPalindrome(-123)
    print(r1)
    r2 = s.isPalindrome(0)
    print(r2)
    r3 = s.isPalindrome(121)
    print(r3)
    r4 = s.isPalindrome(11)
    print(r4)
    r5 = s.isPalindrome(123)
    print(r5)
    r6 = s.isPalindrome(12)
    print(r6)
