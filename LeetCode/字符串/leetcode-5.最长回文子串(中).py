#   给定一个字符串s，找到s中最长的回文子串
#       回文字符串：两侧向中间移动，都是一样的，比如：abcba、abba，都是回文字符串

#   示例1：
#   输入："babad"
#   输出：aba

#   示例2：
#   输入："cbbd"
#   输出：bb

class Solution(object):
    #   方法一：暴力法
    #   遍历每一个子字符串，然后判断这个子字符串是不是回文串，是的话记录，最后得到一个最长的；
    def longestPalindrome_ByForce(self, s):
        max_size = float("-inf")
        max_content = ""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                sub_string = s[i:j+1]
                length,content =self.IsPalindrome(sub_string)
                max_content = max_content if length < max_size else content
                max_size = max_size if length < max_size else length
        return max_size,max_content

    def IsPalindrome(self,s):
        #   这个函数的作用就是判断传入的s是否为"回文字符串"
        left,right = 0,len(s)-1
        while(left<=right):     #   只要左指针<=右指针，就可以left++，right--
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return -1,-1
        return len(s),s

    #   方法二：中心扩展方法
    #   将元素看作是回文字符串的中心，向两边扩展，直到扩展至不相同，但是中心就有两种情况需要考虑：
    #       1、类似：aba，b作为单元素中心；
    #       2、类似：abba，bb作为双元素中心；
    #   从中心向两侧扩展[left>=0、right<=len(s)-1)]，如果s[left]==s[right]则继续扩展，否则就结束了，移动到下一个中心；

    #   这道题用中心扩展方法的时候有几种注意点：
    #       1、一定要考虑到left,right=i,i以及left,right=i,i+1这两种情况(单双元素中心)；
    #       2、向两侧扩展后，注意left和right的值；


    def longestPalindrome_ByCentralExpansion(self, s):
        max_size = float("-inf")
        max_content = ""

        for i in range(0,len(s)):       #   要先判断出当前i的情况下是双中心还是单中心
            left1, right1 = self.longestPalindrome(s,i,i)            #   这个是i的单元素中心的情况
            left2, right2 = self.longestPalindrome(s, i, i+1)        #   这个是i和i+1双元素中心的情况

            #   拿到了i、i+1单元素中心和双元素中心的符合回文串要求的left和right的两组数据，分别进行对比
            if right1+1-left1 > max_size:
                max_size = right1+1-left1
                max_content = s[left1:right1+1]

            if right2+1-left2 > max_size:
                max_size = right2+1-left2
                max_content = s[left2:right2+1]

        return max_size,max_content

    def longestPalindrome(self, s,left,right):
        while(left>=0 and right <=len(s)-1 and s[left] == s[right]):
            left -= 1
            right += 1
        return left+1,right-1       #   left和right就是满足回文子串条件的left和right


s = "aaaaaaa"
max_size,max_content = Solution().longestPalindrome_ByCentralExpansion(s)
print(max_size,max_content)

