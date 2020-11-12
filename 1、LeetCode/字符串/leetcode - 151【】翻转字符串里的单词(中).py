#   给定一个字符串，逐个翻转字符串中的每个单词；

#   说明：
#       无空格字符构成一个单词 。
#       输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#       如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

#   示例1: 
#       输入："the sky is blue"
#       输出："blue is sky the"

class Solution(object):

    def reverseWords(self, s):

        new_s = ""
        end = len(s)
        for i in range(end-1,-1,-1):
            if s[i].isalpha() == True and s[i-1].isalpha() == False:
                # 当找到一个完整的单词范围，则整理出这个单词
                new_s = new_s + s[i:end]



        return new_s



s = "the sky is blue"
result = Solution().reverseWords(s)
print(result)
