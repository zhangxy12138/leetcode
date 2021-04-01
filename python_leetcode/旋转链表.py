# -*-coding:utf-8-*-
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if k == 0 or not head or not head.next:
        return head

    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1

    if (add := n - k % n) == n:
        return head

    cur.next = head
    while add:
        cur = cur.next
        add -= 1

    ret = cur.next
    cur.next = None
    return ret








if __name__ == '__main__':
    # print(2%0)
    # pass


