#   给定一个字符串，逐个翻转字符串中的每个单词；

#   说明：
#       无空格字符构成一个单词 。
#       输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#       如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

#   示例1: 
#       输入："the sky is blue"
#       输出："blue is sky the"

#   示例2：
#       输入："EPY2giL"
#       输出："EPY2giL"
class Solution(object):

    #   注意：数字不作为分割单词的内容，所以不能用isalpha，要用isalnum，判断是否为字母或数字
    #   思路：从后向前进行遍历，将每个单词截取出来，然后放到新的字符串中；
    def reverseWords(self, s):
        new_s = ""
        end = len(s)
        for i in range(end-1,-1,-1):
            if s[i].isalnum() == True and (s[i-1].isalnum() == False or i == 0):        # i=0时，s[i-1]已经不存在，所以要单独进行处理
                # 当找到一个完整的单词范围，则整理出这个单词
                new_s = new_s + s[i:end] + " "
                end = i
            elif (s[i].isalnum() == True and s[i-1].isalnum() == True):
                i -= 1
            else:
                end = i
                i -= 1

        return new_s.strip()



s = "EPY2giL"  # 预期"EPY2giL"
result = Solution().reverseWords(s)
print(result)
