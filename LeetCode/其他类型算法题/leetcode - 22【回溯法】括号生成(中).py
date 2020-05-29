#   LeeCode - 22、两数之和
#   数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合

#   示例：
#
#   输入：n = 3
#   输出：[ "((()))" , "(()())" , "(())()" , "()(())" , "()()()" ]

class Solution:

    #   方法一：暴力法
    #   思路：
    #   1、n组，也就是2n个字符 -> n个"(" + n个")" ，组合起来也就是(2n)^2n，比如n=2，那就共有16种组合方式；
    #   2、我们求出这16个组合方式，然后每个进行判断是否符合要求
    #
    #                                           root
    #                       (                                               )
    #               (               )                                (                    )
    #           (       )       (        )                        (       )           (      )
    #         (   )    (  )    (  )    (  )                      (  )    ( )         (  )   ( )
    #
    #   上面每一个从root到叶子节点的路径就是一个情况，我们要做的就是用代码计算得到这每一种情况

    def generateParenthesis(self, n):
        def generate(A):
            #   2n长度就是n组括号最大长度，无论是全是 ( 还是全是 ) 或是 ( 和 ) 随意组合，反正最长就2n
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans

    #   方法二：回溯法
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


result = Solution().generateParenthesis(5)
print(result)

