#   LeeCode - 77、组合

#   给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合；
#   示例:
#   输入：n = 4, k = 2
#   输出：[ [2,4],[3,4],[2,3],[1,2],[1,3],[1,4] ]

class Solution(object):
    #   方法：回溯法
    #   1、k个数，就表示路径的数量，也就是说当路径达到3个，递归结束；
    #   1-n，也就是可选择范围；
    #   按照回溯公式，搞一下；
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start,tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(start,n):
                backtrack(start+1,tmp+[i+1])
            return res

        backtrack(0,[])

result = Solution().combine(10,2)
print(result)


