#   LeetCode - 141、环形链表
#   思路：使用快慢指针
#   快指针一次走两步，慢指针一次走一步，如果有环，那么一定会出现fast == slow的情况，如果fast为None，表示无环


class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow,fast = head,head
        while (slow != fast):
            slow = slow.next
            fast = fast.next.next
            if slow





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

    s = Solution().hasCycle(nodelist[0])
    print(s.val)