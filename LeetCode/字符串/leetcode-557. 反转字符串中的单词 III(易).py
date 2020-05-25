#   557. 反转字符串中的单词 III
#   给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

#   示例：
#   输入: "Let's take LeetCode contest"
#   输出: "s'teL ekat edoCteeL tsetnoc"

class Solution(object):
    #   思路：
    #   空间换时间，新创建一个变量用来存放反向的字符串
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)-1,-1,-1):
           result = result + s[i]
        return  result

s = "Let's take LeetCode contest"
result = Solution().reverseWords(s)
print(result)