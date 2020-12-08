#   137. 只出现一次的数字 - 第二代
#   给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素；
#
#   解析：相比136题，数组中重复的次数成了三次，异或方法明显不行了

#   示例1:
#       输入: [2,2,3,2]
#       输出: 3

class Solution(object):

    #   方法一（常规方法）：字典进行统计
    def singleNumber(self, nums):
        d = dict()
        for index,value in enumerate(nums):
            d[value] = d.get(value,0) + 1
        return sorted(d.items(),key=lambda i:i[1])[0][0]

    #   方法二：利用位运算符
    def singleNumber_2(self,nums):
        pass


l=[2,2,3,2]
result = Solution().singleNumber(l)
print(result)