#   LeetCode - 142、环形链表Ⅱ
#   要求：给定一个链表，返回链表开始入环的第一个节点。 如果链表无环则返回null
#   思路：
#   1、还是设定slow和fast两个节点，如果有某一时刻相同，则表示有环，如果fast或fast.next为None，表示不存在环；
#   2、假设我们从head到入环点长度为a，然后fast和slow相同点在距离如环点b的地方，那么就有当前等式：(a+b)*2 = fast
#   3、当前fast肯定已经在环上，并且可以得到等式：fast = a + b + nx  (x表示环的长度，n>=1)
#   4、根据3、4可以得到等式：a+b = nx
#   5、这里需要推倒一下，现在我们如果此时：slow从head向前走a，fast从meet点逆向走a，各自走a后的相遇点就是环入口

class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1 = head
                p2 = slow
                while(p1!=p2):
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None

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
            nodelist[i].next = nodelist[0]#   如果指向：nodelist 则表示循环

    s = Solution().detectCycle(nodelist[0])
    print(s.val)