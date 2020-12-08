#   剑指 Offer 39. 数组中出现次数超过一半的数字
#   数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

#   示例：
#   输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
#   输出: 2

class Solution(object):

    #   方法一：
    #   字典计数方法，统计最多的那个
    def majorityElement_Bydict(self, nums):
        new_dict = dict()
        for i in range(0,len(nums)):
            count = new_dict.get(nums[i],1)
            if count > len(nums)/2:
                return nums[i]
            else:
                new_dict[nums[i]] = count + 1
                continue
        return 0

    #   方法二：
    #   排序后，中位数就是要求的解
    def majorityElement_Bysort(self, nums):
        return sorted(nums)[len(nums)//2]

nums = [2,2,1,1,1,2,2]
result = Solution().majorityElement_Bydict(nums)
print(result)

