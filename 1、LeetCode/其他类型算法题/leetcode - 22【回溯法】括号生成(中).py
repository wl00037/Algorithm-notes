#   LeeCode - 22、两数之和
#   数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合

#   示例：
#
#   输入：n = 3
#   输出：[ "((()))" , "(()())" , "(())()" , "()(())" , "()()()" ]

class Solution:

    #   方法一：暴力法：清除2n个index的所有情况，从 (((( 到 )))) 的全部情况，其实暴力法也是用的回溯思维，只不过没有条件限制，把所有情况都回溯出来了
    #   思路：
    #   1、n组，也就是2n个字符 -> n个"(" + n个")" ，组合起来也就是(2n)^2n，比如n=2，那就共有16种组合方式；
    #   2、我们求出这16个组合方式，然后每个进行判断是否符合要求
    #
    #                                           root
    #
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
                if valid(A):                    #   如果是一个递归到最下层的结果，则进行判断，是否是合法的；
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            #   判断思路：如果bal大于0，那么就表示(的数量大于)的数量，只要满足这个条件，就是合理的
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False        #   但凡出现)的数量大于(的数量，这个组合一定非法
            return bal == 0             #   用bal == 0 判断，如果等于0，表示(的数量和)的数量一定是配对的，否则一定出现(和)数量不一致的情况，比关切是(数量大于)数量；
        ans = []
        generate([])
        return ans

    #   方法二：加了合法性条件的回溯法
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)       #   这个地方的递归的意义是：当我们在这个地方选择放一个"("，就递归的去完成当这里放下"("后，后面位置所有的组合排列
                S.pop()
            if right < left:                        #   这个地方表示的是当这里放下的是")"，递归的去完成这里放下")"后，后面位置所有组合的全排列
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()
            #   这里的left < n和right <left是保证了所有排列的前提是满足 "合法性括号的要求的"；
        backtrack([], 0, 0)
        return ans

result = Solution().generateParenthesis(5)
print(result)

