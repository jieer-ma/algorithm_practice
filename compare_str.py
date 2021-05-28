#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/5/28
# desc：比较两个字符串是否相等

def compare_str(str1, str2):
    if str1 == str2:
        return True
    else:
        return False


if __name__ == '__main__':
    result = compare_str('abcdef', 'abefgh')
    print(result)