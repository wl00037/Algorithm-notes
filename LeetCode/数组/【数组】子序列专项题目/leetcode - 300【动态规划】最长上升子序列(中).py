#   300. 最长上升子序列
#   给定一个无序的整数数组，找到其中最长上升子序列的长度。

#   示例：输入[10,9,2,5,3,7,101,18]
#   输出：4

class Solution(object):

    #   方法一：动态规划
    #   思路：dp[i]表示到第i个元素作为最后一个元素时，这个子列表中最长的上升子序列
    #   如：
    #   [10,9,2,5,3]，当到了nums[i]=3时，将3与[10,9,2,5]分别比较，如果比其中一个元素大，表示可以将3放到这个元素作为子序列后的下一个上升值，并且dp[i]+1；
    #   让遍历一遍后，找到作为哪个元素的下一个上升值子序列最长，那么dp[i]就写哪个就可以；
    #   dp[i]：即nums的第i个元素作为子序列最后一个元素，该子序列最长上升元素的长度；

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        if len(nums) == 0 :
            return 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return  max(dp)
