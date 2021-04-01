# -*-coding:utf-8-*-

# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         # 用双指针 pre 和cur,学习如何初始化
#         pre = None
#         cur = head
#         # 遍历列表
#         while cur:  # 同时判定链表是否为空
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre

# 递归解法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归的终止条件是当前为空，或者下一个节点为空
        # 触发终止条件，函数返回 head = 最后一个值=5
        if (head is None) or (head.next is None):
            return head
        # 实现递归
        cur = self.reverseList(head.next)
        # cur = 5
        head.next.next = head
        # 4.next.next=4
        # 5.next =4
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 4.next  = null
        # 每层递归函数返回cur,也就是最后一个节点
        return cur
        # cur = 5 一直是5


if __name__ == '__main__':
    pass

    # a ='00111100'
    # b = '00001101'
    # print(int(a,2))
    # print()