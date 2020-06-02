#   LeeCode - 78、子集

#   给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#   示例:
#   输入：nums = [1,2,3]
#   输出：[ [3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[] ]

class Solution(object):
    #   思路：是不是很像字符串的那道：字符串所有排列情况？没错，所以可以用回溯法
    #   1、确定本次的路径；
    #   2、确定可选择的范围；
    #   3、确定结束递归的条件；

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """




nums = nums = [1,2,3]
result,length = Solution().subsets(nums)
print(result,length)


