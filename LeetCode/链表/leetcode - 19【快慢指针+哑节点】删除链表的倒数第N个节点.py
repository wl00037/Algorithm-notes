#   LeetCode - 19、删除链表的倒数第N个节点
#   给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。

#   示例：
#       给定一个链表: 1->2->3->4->5, 和 n = 2.
#       当删除了倒数第二个节点后，链表变为 1->2->3->5.

#   ⭐   本题默认给的n都是有效的，不会一个节点的链表给一个n=10

class ListNode(object):                         #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #   思路：
    #       1、快指针先走n步，然后slow和fast向前，当fast=None，slow到达倒数第n个
    #       2、删除slow即可
    #       3、不同于找到，本题还需要删除，所以还要记录倒数第K个节点的前一个节点
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        Ya_node = ListNode(None)                        #   哑节点

        fast,slow,tmp = head,Ya_node,Ya_node
        while(n>0):
            fast = fast.next
            n -= 1

        while (fast != None):
            tmp = slow
            slow = slow.next
            fast = fast.next

        #   此时的slow位于倒数第k个节点，tmp位于上一个节点

        return head


if __name__ == "__main__":
    nodelist = []       #   测试用的head
    i = 0
    while(i<6):
        nodelist.append(ListNode(i))
        i += 1
    for i in range(0,len(nodelist)):
        if i<5:
            nodelist[i].next = nodelist[i+1]
        else:
            nodelist[i].next = None     #   如果指向：nodelist 则表示循环
    s = Solution().swapPairs(nodelist[0])

    while s != None:
        print(s.val)
        s = s.next
