#   给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
#   如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#   您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#   示例：
#       输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#       输出：7 -> 0 -> 8
#       原因：342 + 465 = 807

#       输入：(1 -> 8) + (0)
#       输出：1 -> 8
#       原因：81 + 0 = 81

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):             #   指针结构定义
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    #   这道题的几个难点：
    #       1、进位符号；
    #       2、一长一短相加；
    #       3、一长一短相加后有进位需求；
    #       4、加完后最后还有进位需求；

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jw_flag = 0                         #   进位符
        result_head = ListNode(None)        #   哑节点
        tmp = result_head

        while(l1 != None and l2 != None):       #   正常相加，直到l1或者l2有一个结束了，为None
            current_val = (l1.val + l2.val + jw_flag) % 10
            jw_flag = 1 if (l1.val + l2.val + jw_flag) >=10 else 0
            tmp.next = ListNode(current_val)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next

        residue_link = l1 if l1 != None else l2
        while(residue_link != None):
            current_val = (residue_link.val + jw_flag) % 10
            jw_flag = 1 if (residue_link.val + jw_flag) >=10 else 0
            tmp.next = ListNode(current_val)
            tmp = tmp.next
            residue_link = residue_link.next

        if jw_flag == 1:
            tmp.next = ListNode(1)

        return result_head.next


def returnNodelist():
    #   测试用生成的链表的函数
    nodelist = []       #   测试用的head
    i = 0
    while(i<6):
        nodelist.append(ListNode(i))
        i += 1
    for i in range(0,len(nodelist)):
        if i<5:
            nodelist[i].next = nodelist[i+1]
        else:
            nodelist[i].next = None
    return nodelist[0]

if __name__ == "__main__":

    nd1 = returnNodelist()
    nd2 = returnNodelist()

    result = Solution().addTwoNumbers(nd1,nd2)
    while(result != None):
        print(result.val)
        result = result.next
