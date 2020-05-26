#   LeeCode - 1、两数之和
#   给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
#   你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

#   示例:
#       给定 nums = [2, 7, 11, 15], target = 9
#       因为 nums[0] + nums[1] = 2 + 7 = 9 所以返回 [0, 1]

class Solution(object):
    #   方法一：暴力法
    #   思路：得到所有两元素的组合，逐个判断
    def twoSum_ByForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arrange = []
        for i in range(0,len(nums)-1):      #   还是要注意这地方循环的边界
            for j in range(i+1,len(nums)):
                arrange.append([nums[i],nums[j]])
        for l in range(0,len(arrange)-1):
            if sum(arrange[l]) == target:
                return arrange[l]
        return []

    #   方法二：时间换空间 - 利用字典查找时间复杂度为O(1)的特点
    #   思路：遍历每个元素nums[i]，target-nums[i]的值从dict中查找，如果有就返回索引，没有就存入{nums[i]:i}
    def twoSum_ByDict(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict= {}
        for i in range(0,len(nums)):
            cur = target - nums[i]
            if cur in my_dict.keys():
                return [i,my_dict[cur]]     #   返回的是满足和为target的索引位；
            else:
                my_dict[nums[i]] = i
        return []

    #   方法二：时间换空间 - 利用字典查找时间复杂度为O(1)的特点
    #   思路：遍历每个元素nums[i]，target-nums[i]的值从dict中查找，如果有就返回索引，没有就存入{nums[i]:i}
    def twoSum_ByDict(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict= {}
        for i in range(0,len(nums)):
            cur = target - nums[i]
            if cur in my_dict.keys():
                return [i,my_dict[cur]]     #   返回的是满足和为target的索引位；
            else:
                my_dict[nums[i]] = i
        return []



l = [-1,2,1,-4]
target = 0
result = Solution().twoSum_ByDict(l,target)
print(result)

