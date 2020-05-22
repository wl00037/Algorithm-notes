#   LeetCode - 面试题22. 链表中倒数第k个节点
#   思路：使用快慢指针
#   让快指针先到正数第K个，然后一快一慢一次向后，当快指针走到最后一个节点，慢指针就位于倒数第K个节点；


class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        slow,fast = head,head

        while(k-1>0):
            fast = fast.next
            k -=1

        while(fast.next != None):
            fast = fast.next
            slow = slow.next

        return slow

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
            nodelist[i].next = None

    s = Solution().getKthFromEnd(nodelist[0],2)