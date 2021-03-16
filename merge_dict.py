#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：合并两个字典


def dict_merge_1(dict1, dict2):
    merge_dic = {}
    merge_dic.update(dict1)
    merge_dic.update(dict2)

    print(merge_dic)


if __name__ == "__main__":
    dict1 = {'a': '1', 'b': 1}
    dict2 = {'c': 'mmm', 'd': 1234, 'a': '2'}

    dict_merge_1(dict1, dict2)
