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
    #           <目前来看，哑节点适合用于对链表进行增删操时使用>
    #       1、非常类似寻找倒数第K个节点，只不过我们要换一个思路，我们要找到倒数第k+1个节点，然后k+1.next = k+1.next.next 也就等于删除了k节点
    #       2、使用哑节点，为的就是处理 ([1],1) 这种case，
    #           将dummy.next=head，并且slow,fast=dummy,dummy，代码逻辑没有变化，但是保证了不出现([1],1)这类case的报错；
    #
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        slow,fast = dummy,dummy

        while(n+1>0):
            fast = fast.next
            n += 1

        while(fast != None):
            slow = slow.next
            fast = fast.next

        #   此时的slow就到达了 倒数第 n+1 个节点
        slow.next = slow.next.next              #       删除倒数第k个节点

        return dummy.next


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
