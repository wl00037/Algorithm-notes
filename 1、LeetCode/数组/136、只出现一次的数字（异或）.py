#   136. 只出现一次的数字
#   给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

#   示例1:
#       输入: [2,2,1]
#       输出: 1

class Solution(object):

    #   思路：遍历一遍，采用异或，异或最后剩下的值就是出现过一次的值
    def singleNumber(self, nums):
        res = 0
        for i in range(0,len(nums)):
            res = res ^ nums[i]
        return res

l = [2,2,1,1,3,3,5,5,7]
result = Solution().singleNumber(l)
print(result)

