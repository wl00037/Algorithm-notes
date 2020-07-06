#   392.判断子序列
#   给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#   示例 1：s = "abc", t = "ahbgdc"
#   返回 true.

class Solution(object):

    #   while循环，想通过s和t都后推一位，不同t后推一位
    def isSubsequence(self, s, t):
        istart,tstart = 0,0
        while istart<len(s) and tstart<len(t):
            if s[istart] == t[tstart]:
                istart += 1
                tstart += 1
            else:
                tstart += 1
        if istart == len(s):
            return True
        return False


s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s,t))