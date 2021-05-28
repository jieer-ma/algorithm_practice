#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/5/28
# desc：从指定字符串中提取出数字并求和
# 例如：从字符串 bcd765xxyyz87xx 中提取出 765, 87，并求 765 + 87 = 852


def add(str):
    l = len(str)
    n = 0
    sum = 0

    for i in range(0, l):
        if '0' <= str[i] <= '9':
            n = n * 10
            n = int(str[i]) + n
        else:
            sum = sum + n
            n = 0

    sum = sum + n

    return sum


if __name__ == '__main__':
    sum1 = add('bcd765xxyyz87xx')
    print(sum1)
    sum2 = add('bcd765xxyyz87xx60')
    print(sum2)
    sum3 = add('bcd765xxyyz87xx60xxx')
    print(sum3)