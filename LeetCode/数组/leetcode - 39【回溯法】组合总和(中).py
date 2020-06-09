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
    #
    #   方法：回溯法
    #   思路：
    #   1、target分别减去每一个索引位的值，比如targte-2=5，然后从[2,3,6,7]中找到组合起来等于5的
    #   2、再将5分别减去2、3、6、7，然后再从2、3、6、7中找到组合分别为3，2，-1，-2的组合
    #   3、
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        target = target
        print(target)


l = [2,3,6,7]
target = 7
result = Solution().combinationSum(l,target)
print(result)

