#   给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度;若这两个字符串没有公共子序列，则返回0。

#   说明：
#   一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#   例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#

#   示例1: 
#   输入: text1 = "abcde", text2 = "ace"
#   输出: 3       --> 解释: 最长公共子序列是 "ace"，它的长度为 3。

#   示例2：
#   输入: text1 = "abpde", text2 = "ace"
#   输出: 2       --> 解释: 最长公共子序列是 "ae"，它的长度为 2。


class Solution(object):

    def longestCommonSubsequence(self, str1, str2):

        #   为了方便填表，我们将str1作为短的长度短的字符串，将str2作为长度长的字符串;
        #   for嵌套循环，外层为短字符串，内层为长字符串;

        if len(str1)>len(str2):
            str1,str2 = str2,str1

        short_len = len(str1) + 1    # +1 是为了保证base case
        long_len = len(str2) + 1

        #	生成 dp table，根据len1和len2的大小
        dp = [[0]*long_len for i in range(0,short_len)]        #   这里注意生成的矩阵和嵌套for循环，搞反了就会超出范围
        for i in range(1, short_len):
            for j in range(1, long_len):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if str1[i-1] != str2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[short_len-1][long_len-1]

s = Solution().longestCommonSubsequence("abcdef","acf")
print(s)
