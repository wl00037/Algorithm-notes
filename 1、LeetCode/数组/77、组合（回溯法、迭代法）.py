#   LeeCode - 77、组合

#   给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合；
#   示例:
#   输入：n = 4, k = 2；[1,2,3,4]中，返回所有两两组合的子数组
#   输出：[ [2,4],[3,4],[2,3],[1,2],[1,3],[1,4] ]

class Solution(object):
    #   方法：回溯法
    #   1、k个数，就表示路径的数量，也就是说当路径达到3个，递归结束；
    #   2、1-n，也就是可选择范围；
    #   3、按照回溯公式，搞一下；

    #   简单说一下思路，假如给一个n=4,k=3
    #   [1,2,3,4] - 2
    #   [1] -> [2]  -> [3]递归结束，再遍历[4]，得到[1,2,3]和[1,2,4]
    #   [1] -> 第二层遍历到[3] -> [4]  遍历结束，得到[1,3,4]
    #   第一层遍历到[2] -> [3] -> [4]  得到[2,3,4]
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
                backtrack(i+1,tmp+[i+1])
            return res

        return backtrack(0,[])

result = Solution().combine(4,3)
print(result)


