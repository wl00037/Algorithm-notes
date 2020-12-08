#   LeetCode - 141、环形链表
#   思路：使用快慢指针
#   快指针一次走两步，慢指针一次走一步，如果有环，那么一定会出现fast == slow的情况，如果fast为None，表示无环


class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def hasCycle(self, head):
        if head == None or head.next == None:           #   保证head或者head.next不为None
            return False
        slow,fast = head,head.next                      #   快慢指针开始的index必须不同，while要用这个做判断
        while (fast != None and fast.next != None):     #   这里用fast和fast.next判断不为None，主要是因为不能出现fast.next=None时，fast.next.next=None.next报错
            slow = slow.next
            fast = fast.next.next
            if fast == slow:                            #   slow和fast更新后，判断，如果不相同则继续向前，如果fast为空了，那么就不满足循环条件，并且返回False
                return True
        return False

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