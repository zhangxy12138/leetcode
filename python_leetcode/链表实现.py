# -*-coding:utf-8-*-

# 定义节点
class Node(object):
    '''
    单链表的节点
    '''
    def __init__(self,item):
        self.item = item
        self.next = None

# 定义链表(链表需要有首地址指针head)
class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''
        判断列表是否为空
        :return:
        '''
        return self._head is None

    def length(self):
        '''
        链表长度
        :return:
        '''
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None,表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def items(self):
        '''
        遍历列表
        :return:
        '''
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next

    def add(self,item):
        '''
        向链表头部添加元素
        :param item:
        :return:
        '''
        # 新节点
        node = Node(item)
        # 新节点指针指向原头部节点
        node.next = self._head
        # 头部节点指针指向新节点
        self._head = node

    def append(self,item):
        '''
        尾部添加元素
        :param item:
        :return:
        '''
        node = Node(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 是空链表，head指向新节点
            self._head = node
        else:
            # 不是空链表，找到尾部，尾部的next节点指向新节点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node






if __name__ == '__main__':
    # 创建链表
    link_list= SingleLinkList()
    # 创建节点
    node1 = Node(1)
    node2 = Node(2)
    # 将节点添加到链表
    link_list._head = node1
    # 将第一个节点的next指针指向下一节点
    node1.next = node2

    # 访问链表
    print(link_list._head.item) #访问第一个节点
    print(link_list._head.next.item) # 访问第二个节点数据


