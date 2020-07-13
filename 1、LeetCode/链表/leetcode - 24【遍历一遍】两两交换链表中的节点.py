#   LeetCode - 24、两两交换链表中的节点
#   给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

#   要求：
#   你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换

#   示例：给定 1->2->3->4, 你应该返回 2->1->4->3.

#   链表类题目不像数组有多种解决方式，一般就一个最优解，本体的最优解：
#   思路：四个节点一组，每一组都记录上四个一组中的new_head和new_last，前一组的new_last指向后一组的new_head即可
#   (1)->(2)->(3)->(4)  (2)->(1)->(4)->(3)，new_head：2；new_last：3

class ListNode(object):                         #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(-1)        #   还是需要一个哑节点
        dummy.next = head
        prev_node = dummy           #   两两一组，pprev_node节点记录的是上一组里面交换后的second，用来指向下一个两组中的first使用
        while head and head.next:
            first_node = head;
            second_node = head.next;
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node = first_node
            head = first_node.next
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
