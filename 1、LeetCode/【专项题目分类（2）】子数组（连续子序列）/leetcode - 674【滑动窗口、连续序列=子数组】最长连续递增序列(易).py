#   674.最长连续递增序列
#   给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。

#   示例 1:
#   输入: [1,3,5,4,7]
#   输出: 3
#   解释: 最长连续递增序列是 [1,3,5], 长度为3。尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

class Solution(object):

    #方法一：滑动窗口
    #思路：
    #   1、right向右移动，找到满足连续递增序列的地方，直到出现后一个小于前一个的时候停止，保存left-right
    #   2、只要后一个大于前一个，就把left移动到和right一起，然后再次向右滑动；
    #   3、len(nums)==0|1时是特殊情况，需要特殊处理；
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 1
        if len(nums) == 0:
            return 0
        left,right = 0,0
        length = len(nums)
        max_len = float("-inf")
        while(right < length):
            if nums[right] > nums[right-1]:
                max_len = max(max_len, right-left+1)
                right += 1
                continue
            if nums[right] <= nums[right-1]:
                max_len = max(max_len,right-left)
                left = right
                right += 1
        return max_len

l1 = [1,1,1,2,2,2,3,3,3]
l2 = [1,3,5,7]
l3 = [1]
max_len = Solution().findLengthOfLCIS(l3)
print(max_len)