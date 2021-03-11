#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：字符串逆序


'''
 可使用以下三种方法实现：
    (1)切片 [start:end:step]
    (2)reverse 方法
    (3)遍历
'''
def slice_fun(str):
    reverse_str = str[::-1]
    print(reverse_str)


def reverse_str(str):
    str_list = list(str)
    str_list.reverse()
    reverse_str = ''.join(str_list)
    print(reverse_str)


def for_fun(str):
    list_str = []

    for x in range(len(str) - 1, -1, -1):
        list_str.append(str[x])

    print(''.join(list_str))


if __name__ == '__main__':
    slice_fun('hello world!')
    reverse_str('hello world!')
    for_fun('hello world!')