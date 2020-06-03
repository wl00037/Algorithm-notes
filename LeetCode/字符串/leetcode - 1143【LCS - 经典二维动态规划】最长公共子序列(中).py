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

    #   方法一：暴力法思路
    #   
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """