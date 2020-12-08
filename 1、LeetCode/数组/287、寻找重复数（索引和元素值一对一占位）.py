#   给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
#   假设只有一个重复的整数，找出这个重复的数。

#   示例：
#   输入: [1,3,4,2,2]     #   前提：所有元素都在1~4内，共5个索引位，所以必然有一个1~4内的元素重复
#   输出: 2
#

class Solution(object):

    #   思路：
    #   根据题目中给定的前提条件：数字都在 1 到 n 之间（包括 1 和 n），说明是正数，范围也已经确定
    #   将每一个元素放到和其值相等的索引位上，index=0的索引位就是存放交换后的值；
    #   当放到索引位的时候发现索引位上的值已经和索引位匹配，这个就是重复的数；

    def findDuplicate(self, nums):
        while(nums[0] != nums[nums[0]]):
            tmp = nums[nums[0]]
            nums[nums[0]] = nums[0]
            nums[0] = tmp
            #   这里不能用 nums[0],nums[nums[0]] = nums[nums[0]],nums[0]
        return nums[0]

a = [1,3,4,2,2]
result = Solution().findDuplicate(a)
print(result)
