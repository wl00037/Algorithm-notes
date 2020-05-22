#   LeetCode - 876、链表的中间结点
#   思路：使用快慢指针
#   快指针一次走两步，慢指针一次走一步，当快指针走到None


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