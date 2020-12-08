#   409.最长回文串
#   给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串;
#   在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串;

#   注意：假设字符串的长度不会超过 1010

#   输入: "abccccdd"
#   返回：7        ->  我们可以构造的最长的回文串是"dccaccd", 它的长度是 7

class Solution(object):

    #   思路：
    #   满足回文串的可能性（一）：多组成对的字符；
    #   满足回文串的可能性（二）：多组成对的字符 + 一个单个的字符（单个字符在中心）
    #   根据上面的特点，我们可以计算每个字符出现的正数，然后取其最大的成组的值，相加后最多再加一个单一字符，则是可构成的最长回文串
    def longestPalindrome(self, s):
        dict_all = {}
        is_only = 0
        is_cp = 0
        for i in range(0,len(s)):
            dict_all[s[i]] = dict_all.get(s[i],0) + 1       #   如果要查的key不存在则返回value=0

        for key,value in enumerate(dict_all):
            if dict_all[value] % 2 == 1:                    #   兼容"ccc"这种case
                is_only = 1
            if dict_all[value] // 2:
                is_cp = is_cp + (dict_all[value] // 2)
        return is_cp * 2 + is_only

s = "abccccdd"
result = Solution().longestPalindrome(s)
print(result)
