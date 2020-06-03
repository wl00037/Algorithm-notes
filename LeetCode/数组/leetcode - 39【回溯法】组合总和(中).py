#   LeeCode - 39、组合总和
#   给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#   candidates 中的数字可以无限制重复被选取。

#   说明：
#   所有数字（包括 target）都是正整数。
#   解集不能包含重复的组合。

#   示例：
#   输入: candidates = [2,3,6,7], target = 7
#   输出：[ [7], [2,2,3] ]



class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


l = [-1,2,1,-4]
target = 0
result = Solution().twoSum_ByDict(l,target)
print(result)

