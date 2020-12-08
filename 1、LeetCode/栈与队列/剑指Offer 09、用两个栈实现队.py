
#   剑指 Offer 09. 用两个栈实现队列
#   栈：先进后出
#   队列：先进先出
#   本题的目标就是用两个栈，实现先进先出

#   思路1：按照顺序向栈1压入，然后再按照弹出的顺序压入栈2，此时栈2就是按照进入栈1的顺序从上到下，从栈2先弹出的也就是先压入栈1的；
#   思路2：栈1要压入数据时，将栈2作为辅助，压入前将栈1的从上到下全部放到栈2中，然后将本次压入栈1的数据放到最下，再将栈2的数据取回压入栈1；

#   本题采用思路1解决

class CQueue(object):

    #   实现一个栈的数据结构

    def __init__(self):
        self.container = []     #   用来存储栈帧的容器
        self.top = -1           #   标注栈顶的位置，初始化值为1，表示栈为空

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.container.append(value)
        self.top = len(self.container) - 1

    def deleteHead(self):
        """
        :rtype: int
        """
        self.top = self.top - 1
        return self.container.pop(0)        #   默认pop是从列表末位进行弹出，参数0表示从列表首位弹出

    def getContainer(self):
        return self.container

c1 = CQueue()
count = 5
while count > 0 :
    c1.appendTail(count)
    count -= 1

print(c1.getContainer())

c2 = CQueue()

while c1.top != -1:
    c2.appendTail(c1.deleteHead())

print(c2.getContainer())
