#   leetcode - 344、反转字符串
#   题目：编写一个函数，其作用是将输入的字符串反转过来。
#
#   要求：不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用O(1)的额外空间解决这一问题。
#
#   你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

#   示例：
#   输入：["H","a","n","n","a","h"]
#   输出：["h","a","n","n","a","H"]

#   注意！！！！python中字符串为不可变的数据结构，假如我们有：
#       a = "abc";a[1] = "x";
#   这个会报错


class Solution(object):
    #   方法：左右指针，向中间靠拢，left和right互换
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left,right = 0,len(s)-1
        while(left<right):
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return s

s = ["H","a","n","n","a","h"]
result = Solution().reverseString(s)
print(result)