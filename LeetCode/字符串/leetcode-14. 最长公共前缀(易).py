#   leetcode - 14、最长公共前缀
#   编写一个函数来查找字符串数组中的最长公共前缀。 如果不存在公共前缀，返回空字符串 ""。
#
#   示例 1:
#   输入: ["flower","flow","flight"]
#   输出: "fl"

#   示例 2:
#   输入: ["dog","racecar","car"]
#   输出: ""
#   解释: 输入不存在公共前缀。


class Solution(object):
    #   思路：
    #       1、第一步先将list[0]和list[1]得到一个公共前缀；
    #       2、再将这个前缀与list中每一个字符串进行前缀匹配，得到最短前缀；

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = sorted(strs,key=lambda s:len(s))[0]
        for i in range(0,len(strs)):
            print("i的for循环",i)
            l = 0
            while(l < len(prefix)):
                print(l)
                if prefix[l] == strs[i][l]:
                    l += 1
                    continue
                prefix = prefix[0:l]
                break
        return bool(len(prefix)),prefix

strs = ['avabc', 'avd',"avac"]
result = Solution().longestCommonPrefix(strs)
print(result)