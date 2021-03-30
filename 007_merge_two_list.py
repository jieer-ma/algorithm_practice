#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/30
# desc：将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# todo 待确认


# Node 类
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# 实现两个有序链表合并
class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next


if __name__ == '__main__':
    s = Solution()
    a1 = ListNode(1)
    a2 = ListNode(3)
    a3 = ListNode(4)
    a1.next = a2
    a2.next = a3

    a4 = ListNode(1)
    a5 = ListNode(2)
    a6 = ListNode(4)
    a4.next = a5
    a5.next = a6

    r1 = s.mergeTwoLists()
    print(r1)
