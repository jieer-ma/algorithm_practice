#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：计算字符串或列表中每个字符出现的次数，并打印出现次数最多的字符


def calc_max_string(str):
    # 将字符串转化成列表
    str_list = list(str)
    # 定义一个空字典，用来存储 字符: 出现次数
    str_dict = {}

    # 遍历列表(字符串)
    for x in str_list:
        # 如果该字符没有在字典中出现过，则赋值为1，否则在原来基础上+1
        if str_dict.get(x) is None:
            str_dict[x] = 1
        else:
            str_dict[x] = str_dict[x] + 1

    # 输出 { 字符：出现次数 }
    print(str_dict)
    # 找出字典中的 max(values)
    max_str = max(str_dict.values())

    # 遍历字典
    for k,v in str_dict.items():
        # 如果 values = max，打印该字符及出现次数
        if v == max_str:
            print('出现次数最多的字符是：', k, ',一共出现了', v, '次')
        else:
            continue


if __name__ == '__main__':
    calc_max_string('asdfghjkliiuytreqasdccvv')