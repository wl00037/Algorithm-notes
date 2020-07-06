#   给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

#   输入: [-2,1,-3,4,-1,2,1,-5,4],
#   输出: 6
#   解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution(object):

    #   方法一：暴力法，求出所有连续子序列搭配，然后得到最大的和以及最大和的元素
    def maxSubArray_ByForce(self, nums):
        max_sum = float("-inf")
        max_content = []
        for i in range(0,len(nums)):
            for j in range(i,len(nums)-1):
                current_list = nums[i:j+1]
                max_sum = max_sum if max_sum > sum(current_list) else sum(current_list)
                max_content = max_content if max_sum > sum(current_list) else current_list
        return max_sum,max_content

    #   方法二：动态规划【该题目是动态规划的经典题目】
    #   思路：
    #   ⭐ dp数组中索引位i存的值都表示nums数组中以第i个索引位作为连续子数组最后一个元素的数组的最大的和；
    #   之前一直该题动态规划解法不理解，就是没搞明白dp数组内存的值到底是什么；
    def maxSubArray_ByDP(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] + dp[i-1] > nums[i]:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
        return max(dp)

s = [-2,1,-3,4,-1,2,1,-5,4]
max_sum1,max_content = Solution().maxSubArray_ByForce(s)
max_sum2 = Solution().maxSubArray_ByDP(s)
print(max_sum1,max_content,max_sum2)

