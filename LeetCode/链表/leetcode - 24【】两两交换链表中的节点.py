#   LeetCode - 24、两两交换链表中的节点
#   给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

#   要求：
#   你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换

#   示例：给定 1->2->3->4, 你应该返回 2->1->4->3.


class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":

    nodelist = []       #   测试用的head
    i = 0
    while(i<10):
        nodelist.append(ListNode(i))
        i += 1
    for i in range(0,len(nodelist)):
        if i<9:
            nodelist[i].next = nodelist[i+1]
        else:
            nodelist[i].next = None     #   如果指向：nodelist 则表示循环

    s = Solution().hasCycle(nodelist[0])
    print(s)