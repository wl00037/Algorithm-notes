#   LeetCode - 206、反转链表
#   反转一个单链表

#   输入: 1->2->3->4->5->NULL
#   输出: 5->4->3->2->1->NULL


class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    #   其实思路很简单：
    #   1、当前节点要指向上一个节点，所以必须有变量保存上一个节点
    #   2、但是当节点指向了上一个，那么该节点就丢失了链接下一个节点的路，所以在指向上一个节点的时候一定先要保存下一个几点，变量为temp;
    #   3、当前节点永远都是那个：没有指向它的，但是它还指向下一个的节点
    #   (None)  (1) -> (2) -> (3) -> None
    #   当第一次结束后：(None) <- (1)  (2) -> (3) -> None，此时(1)和(2)之间已经断裂，所以在(1)指向前一个之前一定要先保存(1)的next(2)
    #   此时将curr = temp，就将curr移动到(2)上，正常继续处理即可

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        curr = head

        while(curr != None):   #   当head的next为None，也就是说这个是最后一个节点了
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre



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

    s = Solution().reverseList(nodelist[0])
    print(s.val)