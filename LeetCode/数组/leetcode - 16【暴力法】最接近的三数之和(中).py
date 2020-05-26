#   LeeCode - 16、最接近的三数之和
#   题目：给一个数组nums和一个目标值target，从nums中找到三个整数，这三个整数的和最接近target，返回这三个整数和
#
#   例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#   与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

class Solution(object):
    #   方法一：暴力法
    #   思路：组合所有三个数的情况，得到最接近的值；
    def threeSumClosest_ByForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        AllArrangeList = []
        closest = float("inf")
        result = []
        for x in range(0,len(nums)-2):
            for y in range(x+1,len(nums)-1):
                for z in range(y+1,len(nums)):
                    AllArrangeList.append([nums[x],nums[y],nums[z]])
        for i in range(0,len(AllArrangeList)-1):
            if  abs(sum(AllArrangeList[i]) - target) < closest:
                closest = sum(AllArrangeList[i])
                result = AllArrangeList[i]

        return closest,result

l = [-1,2,1,-4]
target = 1
closest,result = Solution().threeSumClosest_ByForce(l,target)
print(closest,result)

