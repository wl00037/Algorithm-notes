#   LeeCode - 39、组合总和Ⅰ
#   给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#   candidates 中的每个数字在每个组合中只能使用一次。

#   说明：
#   所有数字（包括 target）都是正整数    -> 注意这个要求，如果candidates包括负数，这个就非常不好解决了
#   解集不能包含重复的组合。

#   示例：
#   输入: candidates = [10,1,2,7,6,1,5], target = 8,
#   输出：[ [1, 7],[1, 2, 5],[2, 6],[1, 1, 6] ]

class Solution(object):
    #   方法：回溯法
    #   思路：
    #   基本和 leetcode - 39 非常类似，只不过回溯过程有点区别，就是不允许对当前本身索引位的值进行回溯
    #   难点：去重，比如上面例子的[1,7]和[7,1]

    def combinationSum1(self, candidates, target):
        """
            Leetcode上的执行超出时间
        """
        res = []
        n = len(candidates)
        def backtrack(candidates,path,target,start):
            if sum(path) == target:
                if path not in res:     #   这个地方的in会造成超时
                    res.append(path)
            for i in range(start,n):
                backtrack(candidates,path+[candidates[i]],target,i+1)
        backtrack(candidates,[],target,0)
        return res

    def combinationSum2(self, candidates, target):
        """
            1、使用同层去重的逻辑：排序后，同一层的递归相邻两个元素如果相同，不进行处理；
            2、超过target本身的元素不进行处理；
            3、如果sum(path)>target，本次递归结束
            Leetcode上的执行超出时间
        """
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(candidates,path,target,start):
            if sum(path) == target:
                res.append(path)

            for i in range(start,n):
                if candidates[i] > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:      #   这个就是重点：同层去重，当i>start，一定是在一层中进行的遍历
                    continue
                backtrack(candidates,path+[candidates[i]],target,i+1)

        backtrack(candidates,[],target,0)
        return res


l = [10,1,2,7,6,1,5]
target = 8
result = Solution().combinationSum2(l,target)
print(result)

