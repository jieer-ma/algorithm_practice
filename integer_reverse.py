#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/18
# desc：整数反转
#       给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#       如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。


def reverse_integer(num):
    # 将数字转化成字符串
    str_num = str(num)

    # 判断数字是否超出存储范围
    if num > (2 ** 31):
        print(num, '超出整数可存储最大值')
        return 0
    if num < (-2 ** 31):
        print(num, '超出整数可存储最小值')
        return 0

    # 反转字符串
    reverse_str_num = str_num[::-1]

    # 检查反转后的字符串中是否含有 -，有的话 si_true = index('-')， 没有的话 si_true = -1
    si_true = reverse_str_num.find('-')

    # 如果反转后的字符串中有 -，将其删除(因为此时 -在最后)
    if si_true >= 0:
        reverse_list_num = list(reverse_str_num)
        reverse_list_num.remove('-')
        reverse_str_num = ''.join(reverse_list_num)
        reverse_str_num = '-' + reverse_str_num

    # 将字符串数字转化成整数
    reverse_int_num = int(reverse_str_num)

    print(num, ' 反转后是：', reverse_int_num)
    return reverse_int_num


if __name__ == '__main__':
    reverse_integer(123)
    reverse_integer(-123)
    reverse_integer(2 ** 31)
    reverse_integer(-2 ** 31)
    reverse_integer(2 ** 31 + 1)
    reverse_integer(-(2 ** 31 + 1))



