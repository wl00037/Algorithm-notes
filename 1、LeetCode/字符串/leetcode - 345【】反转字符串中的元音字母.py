#   leetcode-345 编写一个函数，以字符串作为输入，反转该字符串中的元音字母
#
#   示例：
#   输入："leetcode"
#   输出："leotcede"
#
#   元音：['a','e','i','o','u']

class Solution(object):

    #   思路：
    #   两个指针向中间移动，right向前找到元音后，left向后找到对应元音字母交换，直到两个指针相遇或right<left，则表示交换完毕；
    #   元音：['a','e','i','o','u','A','E','I','O','U']
    def reverseVowels(self, s):
        target = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        left,right = 0,len(s)-1
        while left != right and left < right:
            if s[right] not in target:
                right -= 1
                continue

            if s[right] in target:
                while s[left] not in target:
                    left += 1

            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            right -= 1
            left += 1
        return str(s)

s = "leetcode"
result = Solution().reverseVowels(s)
print(type(result),result)