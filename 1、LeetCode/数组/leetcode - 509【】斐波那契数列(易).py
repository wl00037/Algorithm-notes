#   509. 斐波那契数

#   斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#   F(0) = 0,   F(1) = 1
#   F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

#   给定 N，计算 F(N)，计算的就是第N个的值

class Solution(object):

    def fib(self, N):
        if N == 0: return 0             # 对N=0做单独处理，N=1不需要
        result = [0,1]
        start = 2
        tmp = N + 1 - 2     #   参数4是指：索引位的4，而不是第四个数，所以要向后加一
        while tmp > 0:
            result.append(result[start-1] + result[start-2])
            tmp -= 1
            start += 1
        return result[start-1]

result = Solution().fib(1)
print(result)

