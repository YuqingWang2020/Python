"""
21. Merge Two Sorted Lists
Y.Wang
Date: 15.07.2021
python 没有指针的概念，在python中每个变量都是指针
实现链表总体需要两步
1.定义链表:
2.对链表进行操作
"""

"""
1.定义链表:
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
2.对链表进行操作
"""
class LinkList:
   # def __init__(self):
   #     self.head=None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r=self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    def printlist(self,head):
        # 打印链表
        if head == None: return
        node = head
        while node != None:
            print(node.val,end=' ')
            node = node.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        p=dummy
        while l1 and l2:
            if l1.val<l2.val:
                p.next=l1
                l1=l1.next
            else:
                p.next=l2
                l2=l2.next
            p=p.next
        p.next=l1 or l2
        return dummy.next

if __name__ == '__main__':
    a = Solution()
    l=LinkList()
    data1 = [1, 2, 4]
    data2= [1, 3, 4]
    l1=l.initList(data1)
    l2=l.initList(data2)
    l.printlist(l1)
    print("\r")
    l.printlist(l2)
    print("\r")
    m=a.mergeTwoLists(l1,l2)
    l.printlist(m)

