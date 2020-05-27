#   LeeCode - 22、两数之和
#   数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合

#   示例：
#
#   输入：n = 3
#   输出：[ "((()))" , "(()())" , "(())()" , "()(())" , "()()()" ]

class Solution:
    def generateParenthesis(self, n):
        def generate(A):
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

result = Solution().generateParenthesis(5)
print(result)

