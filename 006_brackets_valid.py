#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/11
# desc：给定一个字符串，判断字符串中的括号是否成对


def is_valid(str):
    # 新建括号匹配字典
    brackets = { ')': '(', ']': '[', '}': '{' }
    # 左/右括号
    left_brackets = brackets.values()
    right_brackets = brackets.keys()

    # 空数组(模拟空栈)
    stack = []

    # 遍历字符串
    for x in str:
        # 如果是左括号，进栈
        if x in left_brackets:
            stack.append(x)
        # 如果是右括号，判断栈是否为空&&栈顶元素和右括号是否匹配，匹配左括号出栈，否则括号不匹配，直接 return
        elif x in right_brackets:
            if stack and (stack[-1] == brackets[x]):
                stack.pop(-1)
            else:
                return False

    # 右括号遍历完，判断左括号是否为空，如果不为空则证明括号匹配
    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    r1 = is_valid('{ccc[dddkkkk(ook)]}')
    print(r1)

    r2 = is_valid('}hhgj{(hhgj)[hhgj]')
    print(r2)

    r3 = is_valid('{anh[ddd](djjjjkkk)}}')
    print(r3)

    r4 = is_valid('{anh[ddd]((djjjjkkk)}')
    print(r4)

    r5 = is_valid('[')
    print(r5)