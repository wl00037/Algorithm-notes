#   674.最长连续递增序列
#   给定一个未经排序的整数数组，找到最长且连续递增的子序列，并返回该序列的长度。
#   
#   示例 1:
#   输入: [1,3,5,4,7]
#   输出: 3
#   解释: 最长连续递增序列是 [1,3,5], 长度为3。尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

class Solution(object):

    # 方法：滑动窗口
    # 思路：
    # 1.
    # 2.
    # 3.
    def findLengthOfLCIS(self, nums):

        if not nums:
            return 0

        ans_list = []       # 存放所有最长递增子序列
        ans_length = 1      # 存放当前最长递增子序列的长度
        start = 0

        for i in range(len(nums)-1):
            
            if nums[i+1] > nums[i]:
                ans_length = max(ans_length,i+1-start+1)
            else:
                # 当nums[i+1] <= nums[i]，则上一个连续上升子序列已经终结
                # start=i+1，表示开始下一个连续上升子序列的查找，而i+1就是待寻找的连续上升子序列的首元素
                start = i + 1   

        return ans_length


if __name__ == "__main__":
    l1 = [1,1,1,2,2,2,3,3,3]
    l2 = [1,3,5,4,7]
    max_len = Solution().findLengthOfLCIS(l2)
    print(max_len)
