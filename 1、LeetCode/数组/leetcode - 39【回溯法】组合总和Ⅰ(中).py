#   LeeCode - 39、组合总和Ⅰ
#   给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#   candidates 中的数字可以无限制重复被选取。

#   说明：
#   所有数字（包括 target）都是正整数    -> 注意这个要求，如果candidates包括负数，这个就非常不好解决了
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
    #   3、再次注意，candidates和target全部为正整数
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(candidates)

        def backtrack(candidates,path,target,start):
            if target == 0 :
                res.append(path)
            if target < 0 :             #   根据条件：所有candidates和target全为正整数，如果target<0.一定无解
                return
            for i in range(start,n):
                backtrack(candidates,path+[candidates[i]],target-candidates[i],i)   #   注意，这个地方下一个开始深层递归的start应该是i

        backtrack(candidates,[],target,0)
        return res



l = [2,3,6,7]
target = 7
result = Solution().combinationSum(l,target)
print(result)

