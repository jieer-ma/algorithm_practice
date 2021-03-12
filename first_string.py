#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：给一个字符串找出第一个只出现一次的字符位置


def first_string(str):
    str_list = list(str)
    str_dict = {}

    # 遍历字符串，并按 字符:出现次数 存储到 str_dict 中
    for x in str_list:
        if str_dict.get(x) is None:
            str_dict[x] = 1
        else:
            str_dict[x] = str_dict[x] + 1

    # 将每个字符出现次数按照倒序排序并存储到 str_count 中(可以不排序直接存储)
    str_count = sorted(str_dict.values(), reverse = False)

    # 打印字典
    print(str_dict)

    # 判断有没有出现1次的字符
    if 1 not in str_count:
        print('没有只出现1次的字符')
        return

    # 遍历字典，找出第一个出现1次的字符，并退出程序
    for k,v in str_dict.items():
        if v == 1:
            print('第一个出现一次的字符是：', k)
            return


if __name__ == '__main__':
    first_string('fghjklffhj')
    first_string('ffff')
    first_string('abcd')